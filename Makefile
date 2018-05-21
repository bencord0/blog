test:
	python -m pytest ${TEST_ARGS:tests}

coverage:
	coverage run --source blog -m pytest tests
	coverage report

build-for-registry:
	docker build -t registry.condi.me/blog .
	docker push registry.condi.me/blog

.PHONY: coverage test
