build: docker.tar

run: docker.tar
	./run.sh

test:
	python -m pytest ${TEST_ARGS:tests}

coverage:
	coverage run --source blog -m pytest tests

docker.tar:
	./build.sh

.PHONY: coverage build run test
