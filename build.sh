#!/bin/bash
docker run -v $PWD:/volume -w /volume -t clux/muslrust cargo build

TARGET=target/x86_64-unknown-linux-musl/debug/blog
cp -v "${TARGET}" "docker/blog"
docker build -t bencord0/blog:rust docker
