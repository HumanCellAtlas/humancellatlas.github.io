ENVIRONMENTS := dev integration staging prod

default: site

.PHONY: clean
clean:
	git clean -fd

.PHONY: target
target:
	mkdir -p $(ENVIRONMENT)

.PHONY: page
page:
	python3 build_index_html.py $(ENVIRONMENT) > $(ENVIRONMENT_DIR)/index.html

.PHONY: site
site:
	for e in $(ENVIRONMENTS); do \
		$(MAKE) target ENVIRONMENT=$$e; \
		$(MAKE) page ENVIRONMENT=$$e ENVIRONMENT_DIR=./$$e; \
	done
	$(MAKE) page ENVIRONMENT=$$e ENVIRONMENT_DIR='.'; \
