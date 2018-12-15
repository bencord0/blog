blog.condi.me
-------------

This is a reimplementation of my blog in python (django).

Getting started
---------------

1/. Run the blog engine

  $ git clone https://github.com/bencord0/blog -b python-django
  $ git clone https://github.com/bencord0/blogposts

  $ cd blog

  # Create and enter the virtualenv
  # You may need to install `pg_config` first, to build the postgres driver.
  $ pipenv install --deploy && pipenv shell

  # The `blog` command is now availble inside the virtualenv shell.
  $ blog manage migrate
  $ blog manage collectstatic
  $ blog manage import_entries ../blogposts

  # Run the webserver
  $ export ALLOWED_HOSTS=localhost
  $ blog -b 0.0.0.0:8000

2/. Report inconsistencies with the live site, and make suggestions.

Docker
------

Build docker image, setup a database and import blogposts.

  $ make compose{-migrate,-import}

To run the webserver:

  $ make web

It will be available on http://localhost:8000/

Running Tests
-------------

  # Install development dependencies
  $ pipenv install --dev

Invoke `tox` without arguments.
        This runs the full test suite, the flake8 linter
        and produces a coverage report.
        This form is useful in CI environments.

Invoke `make test`,
    or `make test TEST_ARGS=tests`
        This runs the full test suite using the current environment,
        or a subset of the tests if you specify `TEST_ARGS`.

Finally `make coverage`.
        Like `make test` this will run the full test suite, but
        will also produce a coverage report at the end.
