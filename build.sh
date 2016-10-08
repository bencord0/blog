#!/bin/bash
set -ex

if [ ! -d venv ]; then
	python -m virtualenv venv
fi

source venv/bin/activate

pip install -U pip tox

tox
