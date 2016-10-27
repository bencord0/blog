#!/bin/bash
set -xe

if [ ! -d venv ]; then
  # Require any modern python implementation
  python -m virtualenv venv
fi

source venv/bin/activate
pip install --upgrade -r requirements.txt
pex -vv -o blog.pex --no-wheel --disable-cache . -m blog

mkdir -p dist/etc dist/usr/lib64
echo 'hosts: files dns' > dist/etc/nsswitch.conf
cp -a /usr/lib64/postgresql/libpq.so* dist/usr/lib64/
cp -a /usr/lib/libldap-2.4.so.2* dist/usr/lib64/
cp -a /usr/lib64/liblber-2.4.so.2* dist/usr/lib64

docker build -t bencord0/blog .
docker save bencord0/blog > docker-blog.tar
