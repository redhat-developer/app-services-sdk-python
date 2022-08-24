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
	@curl -sSL https://install.python-poetry.org | python -
	@$HOME/.local/bin
endif

.PHONY: build 
build: install-setup
	@poetry build

.PHONY: publish
publish: install-setup 
	@twine upload dist/*