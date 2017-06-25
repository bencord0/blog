#!/bin/bash
set -xe

docker build -t bencord0/blog .
docker save -o docker.tar bencord0/blog
