extern crate blog;

extern crate getopts;
extern crate pencil;

use getopts::Options;
use pencil::Pencil;
use std::env;

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

  app.get("/", "index", blog::index);
  app.get("/<slug>/", "slug", blog::slug);


  let listen = format!("{}:{}", bind, port);
  let listen_str = listen.as_str();
  println!("Listening on {}", listen);
  app.run(listen_str)
}
