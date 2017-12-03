test:
	python -m pytest ${TEST_ARGS:tests}

coverage:
	coverage run --source blog -m pytest tests
	coverage report

.PHONY: coverage test
