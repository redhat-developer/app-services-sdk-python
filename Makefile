.PHONY: generate
generate:
	./scripts/generate.sh

.PHONY: generate-errors
generate-errors:
	./scripts/errors/generate-errors.sh

.PHONY: build
build:
	@{ \
		poetry build \
		}
	

.PHONY: publish
publish:
	@{ \
		poetry publish ;\
	}