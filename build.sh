#!/bin/bash
set -xe

if [ ! -d venv ]; then
  # Require any modern python implementation
  python -m venv venv
fi

source venv/bin/activate
pip install --upgrade -r requirements.txt
pex -vv -o blog.pex --no-wheel --disable-cache . -m blog

docker build -t bencord0/blog .
docker save bencord0/blog > docker-blog.tar
