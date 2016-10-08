#!/bin/bash
source venv/bin/activate

python setup.py bdist_wheel
pip wheel --wheel-dir dist twisted

docker build -t blog .
