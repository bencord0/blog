TEST_ARGS ?= tests
test:
	python -m pytest $(TEST_ARGS)

coverage:
	coverage run --source blog -m pytest tests
	coverage report
	coverage html

build-for-registry:
	docker build -t registry.condi.me/blog .
	docker push registry.condi.me/blog

.PHONY: coverage test
