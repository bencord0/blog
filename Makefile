docker: docker.tar

pex: blog.pex

run: docker.tar
	./run.sh

test:
	python -m pytest ${TEST_ARGS:tests}

coverage:
	coverage run --source blog -m pytest tests
	coverage report

docker.tar:
	./build.sh

blog.pex:
	pip install -r build-requirements.txt
	pex  -vv -o blog.pex --no-wheel --disable-cache . -m blog

.PHONY: coverage docker pex run test
