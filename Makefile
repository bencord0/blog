TEST_ARGS ?= tests
test:
	python -m pytest $(TEST_ARGS)

coverage:
	coverage run --source blog -m pytest $(TEST_ARGS)
	coverage report
	coverage html

build-for-registry:
	docker build -t registry.condi.me/blog .
	docker push registry.condi.me/blog

COMPOSE_ARGS := ""
web:             COMPOSE_ARGS=-b 0.0.0.0:8000
compose-migrate: COMPOSE_ARGS=manage migrate
compose-import:  COMPOSE_ARGS=manage import_entries /blogposts

compose compose-migrate compose-import web:
	docker-compose run \
	    --rm --service-ports \
	    -v $(pwd)/../blogposts:/blogposts \
		blog \
		pipenv run blog $(COMPOSE_ARGS)

.PHONY: coverage test
