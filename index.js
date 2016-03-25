var express = require('express');
var fs = require('fs');
var nunjucks = require('nunjucks');
var glob = require('glob-fs')();
var Markdown = require('node-markdown').Markdown;
var app = express();

nunjucks.configure('templates', {
  autoescape: true,
  express: app
});

app.get('/', function(request, response) {
  files = glob.readdirSync('metadata/*.json');

  entries = {};
  files.map(function(file) {
    entry = JSON.parse(fs.readFileSync(file));
    entries[entry.date] = entry;
  });

  recent_entries = [];
  Object.keys(entries).sort().reverse().map(function(date) {
    recent_entries.push(entries[date]);
  });

  response.render('index.html', {
    'recent_entries': recent_entries
  });
});

app.get('/:slug/', function(request, response) {
  slug = request.params.slug;

  meta = JSON.parse(fs.readFileSync('metadata/' + slug + '.json'))

  fs.readFile('markdown/' + slug + '.md',
              {encoding: 'utf-8'},
              function(err, data) {
    if (err) throw err;
    response.render('entry.html', {
      'html': Markdown(data),
      'entry': meta,
    });
  });
});

app.set('port', (process.env.PORT || 8000));
app.listen(app.get('port'), function() {
  console.log('Blog is running on port', app.get('port'));
});
