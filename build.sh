#!/bin/bash
set -xe

if [ ! -d venv ]; then
  # Require any modern python implementation
  python -m virtualenv venv
fi

source venv/bin/activate
pip install --upgrade -r requirements.txt
pex -vv -o blog.pex --disable-cache . -m blog
