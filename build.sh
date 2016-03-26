#!/bin/bash
set -xe

if [ ! -d venv ]; then
  # Try suitable virtualenv implementations
  # in order of preference.
  pyvenv venv || pyvenv-3.5 venv || pyvenv-3.4 venv || virtualenv venv
fi

source venv/bin/activate
pip install -r requirements.txt
pip install -e .
pex -vv -o blog.pex --disable-cache . -m blog
