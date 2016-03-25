extern crate getopts;
extern crate glob;
extern crate hoedown;
extern crate pencil;
extern crate rustc_serialize;

use getopts::Options;
use glob::glob;
use hoedown::{Markdown, Render};
use hoedown::renderer::html::{Flags, Html};
use pencil::Pencil;
use pencil::{Request, PencilResult};
use rustc_serialize::json::{self, ToJson, Json};
use std::collections::BTreeMap;
use std::env;
use std::fs::File;
use std::io::Read;

#[derive(RustcDecodable, RustcEncodable)]
struct MetaData {
  date: String,
  slug: String,
  title: String,
}

impl ToJson for MetaData {
    fn to_json(&self) -> Json {
        let mut obj = BTreeMap::new();
        obj.insert("date".to_string(), self.date.to_json());
        obj.insert("slug".to_string(), self.slug.to_json());
        obj.insert("title".to_string(), self.title.to_json());
        Json::Object(obj)
    }
}

fn index(request: &mut Request) -> PencilResult {
  println!("[{}]{}", request.method(), request.path().unwrap());

  let mut entries = BTreeMap::new();
  let mut recent_entries: Vec<MetaData> = Vec::new();

  for entry in glob("metadata/*.json").unwrap() {
    let entry = entry.unwrap();
    let mut entry_f = File::open(entry).unwrap();
    let mut entry_r = String::new();
    let _ = entry_f.read_to_string(&mut entry_r);
    let md: MetaData = json::decode(entry_r.as_str()).unwrap();

    entries.insert(md.date.clone(), md);
  }

  for (_, meta) in entries.into_iter() {
    recent_entries.push(meta);
  }
  recent_entries.reverse();

  let mut context = BTreeMap::new();
  context.insert("recent_entries".to_string(), recent_entries);

  match request.app.render_template("index.html.hb", &context) {
    Ok(x) => Ok(x),
    Err(x) => { println!("{:?}", x); Err(x) },
  }
}

fn slug(request: &mut Request) -> PencilResult {
  println!("[{}]{}", request.method(), request.path().unwrap());
  let slug = request.view_args.get("slug").unwrap();

  let meta = format!("metadata/{}.json", slug);
  let mut meta_f = File::open(meta).unwrap();
  let mut meta_r = String::new();
  let _ = meta_f.read_to_string(&mut meta_r);
  let metadata: MetaData = json::decode(meta_r.as_str()).unwrap();

  let mark = format!("markdown/{}.md", slug);
  let mut mark_f = File::open(mark).unwrap();
  let mut mark_r = String::new();
  let _ = mark_f.read_to_string(&mut mark_r);
  let markdown = Markdown::new(mark_r.as_str());


  let mut html = Html::new(Flags::empty(), 0);
  let mut context = BTreeMap::new();
  context.insert("entry".to_string(), metadata.to_json());
  // XXX: impl ToJson for hoedown::buffer::Buffer
  context.insert("html".to_string(), html.render(&markdown).to_str().unwrap().to_json());

  match request.app.render_template("entry.html.hb", &context) {
      Ok(x) => Ok(x),
      Err(x) => { println!("{:?}", x); Err(x) },
  }
}

fn main() {
  let args: Vec<String> = env::args().collect();

  let mut opts = Options::new();
  opts.optopt("b", "bind", "Address to bind to", "BIND");
  opts.optopt("p", "port", "Port to bind to", "PORT");

  let matches = match opts.parse(&args[1..]) {
    Ok(m) => { m }
    Err(f) => { panic!(f.to_string()) }
  };

  let bind = match matches.opt_str("bind") {
    Some(x) => x,
    None => env::var("BIND").unwrap_or("127.0.0.1".to_string())
  };

  let port = match matches.opt_str("p") {
    Some(x) => x,
    None => env::var("PORT").unwrap_or("8000".to_string())
  };

  let mut app = Pencil::new("./");
  app.set_debug(true);
  app.set_log_level();
  app.enable_static_file_handling();

  app.register_template("index.html.hb");
  app.register_template("entry.html.hb");

  app.get("/", "index", index);
  app.get("/<slug>/", "slug", slug);


  let listen = format!("{}:{}", bind, port);
  let listen_str = listen.as_str();
  println!("Listening on {}", listen);
  app.run(listen_str)
}
