.PHONY: generate
generate:
	./scripts/generate.sh

.PHONY: generate-errors
generate-errors:
	./scripts/errors/generate-errors.sh

.PHONY: publish
publish:
	./scripts/publish.sh