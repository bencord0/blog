extern crate glob;
extern crate hoedown;
extern crate pencil;
extern crate rustc_serialize;

use glob::glob;
use hoedown::{Markdown, Render};
use hoedown::renderer::html::{Flags, Html};
use pencil::{Request, PencilResult};
use rustc_serialize::json::{self, ToJson, Json};
use std::collections::BTreeMap;
use std::fs::File;
use std::io::Read;

#[derive(RustcDecodable, RustcEncodable)]
struct MetaData {
  date: String,
  slug: String,
  title: String,
}

#[derive(RustcDecodable, RustcEncodable)]
struct Entry {
  meta: MetaData,
  //md: String,
  html: String,
  summary: String,
}

impl Entry {
  fn new(meta: MetaData) -> Entry {
    let mark = format!("markdown/{}.md", meta.slug);
    let mut mark_f = File::open(mark).unwrap();
    let mut mark_r = String::new();
    let _ = mark_f.read_to_string(&mut mark_r);
    let markdown = Markdown::new(mark_r.as_str());

    let mut html_renderer = Html::new(Flags::empty(), 0);
    let html: String = html_renderer.render(&markdown).to_str().unwrap_or("").to_string();
    let mut summary_vec: Vec<&str> = html.split("</p>").collect();
    // Vec.swap_remove is O(1)
    let summary: String = summary_vec.swap_remove(0).to_string();

    Entry {
      meta: meta,
      //md: markdown,
      html: html.clone(),
      summary: summary,
    }
  }
}

impl ToJson for Entry {
    fn to_json(&self) -> Json {
        let mut obj = BTreeMap::new();
        obj.insert("date".to_string(), self.meta.date.to_json());
        obj.insert("slug".to_string(), self.meta.slug.to_json());
        obj.insert("title".to_string(), self.meta.title.to_json());
        //obj.insert("md".to_string(), self.md.to_json());
        obj.insert("html".to_string(), self.html.to_json());
        obj.insert("summary".to_string(), self.summary.to_json());
        Json::Object(obj)
    }
}

fn get_recent_entries(count: usize) -> Vec<Json> {
  let mut entries = BTreeMap::new();
  let mut recent_entries: Vec<Json> = Vec::new();

  for _meta in glob("metadata/*.json").unwrap() {
    let _meta = _meta.unwrap();
    let mut entry_f = File::open(_meta).unwrap();
    let mut entry_r = String::new();
    let _ = entry_f.read_to_string(&mut entry_r);
    let meta: MetaData = json::decode(entry_r.as_str()).unwrap();

    let entry: Entry = Entry::new(meta);
    entries.insert(entry.meta.date.clone(), entry);
  }

  for (_, meta) in entries.into_iter() {
    recent_entries.push(meta.to_json());
  }

  recent_entries.reverse();
  recent_entries.truncate(count);
  recent_entries
}

pub fn index(request: &mut Request) -> PencilResult {
  println!("[{}]{}", request.method(), request.path().unwrap());

  let recent_entries = get_recent_entries(10);
 
  let mut context: BTreeMap<String, Json> = BTreeMap::new();
  context.insert("recent_entries".to_string(), recent_entries.to_json());

  match request.app.render_template("index.html.hb", &context) {
    Ok(x) => Ok(x),
    Err(x) => { println!("{:?}", x); Err(x) },
  }
}

pub fn slug(request: &mut Request) -> PencilResult {
  println!("[{}]{}", request.method(), request.path().unwrap());
  let slug = request.view_args.get("slug").unwrap();

  let mut entry_f = File::open(format!("metadata/{}.json", slug)).unwrap();
  let mut entry_r = String::new();
  let _ = entry_f.read_to_string(&mut entry_r);
  let meta: MetaData = json::decode(entry_r.as_str()).unwrap();

  let entry: Entry = Entry::new(meta);
  let recent_entries = get_recent_entries(10);

  let mut context = BTreeMap::new();
  context.insert("entry".to_string(), entry.to_json());
  context.insert("recent_entries".to_string(), recent_entries.to_json());

  match request.app.render_template("entry.html.hb", &context) {
      Ok(x) => Ok(x),
      Err(x) => { println!("{:?}", x); Err(x) },
  }
}
