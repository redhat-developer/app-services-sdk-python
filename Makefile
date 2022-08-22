.PHONY: generate
generate:
	./scripts/generate.sh

.PHONY: generate-errors
generate-errors:
	./scripts/errors/generate-errors.sh

.PHONY: install-setup
install-setup:
ifeq (, $(shell which python3 2> /dev/null))
	@echo "python3 is not available, please install it to be able to install poetry for the build"
	exit 1
endif
ifeq (, $(shell which poetry 2> /dev/null))
	@curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
endif

.PHONY: build 
build: install-setup
	@poetry build

.PHONY: publish
publish: install-setup 
	@poetry publish 