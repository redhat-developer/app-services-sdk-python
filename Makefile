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
endif

.PHONY: build 
build: install-setup
	@poetry build

.PHONY: publish
publish: install-setup 
	@twine upload dist/*

# The staggered make target explanations are printed correctly (not staggered) to the console.
.PHONY: help
help:
		@echo "App servces Python SDK make targets" 
		@echo "" 																				
		@echo "make generate			Uses OpenAPI Generator to generate the SDK" 
		@echo "make generate-errors		Generate the SDK errors"
		@echo "make install-setup		Installs poetry"
		@echo "make build			Build the SDK"					
		@echo "make publish			Publish the SDK"
		@echo "make help 			Print this help"