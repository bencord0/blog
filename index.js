var express = require('express');
var fs = require('fs');
var nunjucks = require('nunjucks');
var glob = require('glob-fs')();
var Markdown = require('node-markdown').Markdown;
var app = express();

njk = nunjucks.configure('templates', {
  autoescape: true,
  express: app
});

njk.addGlobal('static', function(thing) {
  return '/static/' + thing;
});

function get_recent_entries(count) {
  var recent_entries = [];
  Object.keys(entries_by_date).sort().reverse().map(function(date) {
    recent_entries.push(entries_by_date[date]);
  });

  return recent_entries.slice(0, count);
}

app.get('/', function(request, response) {
  recent_entries = get_recent_entries(10);
  response.render('index.html.j2', {
    'recent_entries': recent_entries,
  });
});

app.get('/:slug/', function(request, response) {
  slug = request.params.slug;

  meta = entries_by_slug[slug];

  fs.readFile('markdown/' + slug + '.md',
              {encoding: 'utf-8'},
              function(err, data) {
    if (err) throw err;

    recent_entries = get_recent_entries(10);
    response.render('entry.html.j2', {
      'html': Markdown(data),
      'entry': meta,
      'recent_entries': recent_entries,
    });
  });
});


files = glob.readdirSync('metadata/*.json');
entries_by_date = {};
entries_by_slug = {};
files.map(function(file) {
  entry = JSON.parse(fs.readFileSync(file));
  entries_by_date[entry.date] = entry;
  entries_by_slug[entry.slug] = entry;
});


app.set('port', (process.env.PORT || 8000));
app.use('/static', express.static('static'));
app.listen(app.get('port'), function() {
  console.log('Blog is running on port', app.get('port'));
});
