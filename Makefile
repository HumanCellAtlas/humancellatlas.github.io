ENVIRONMENTS := dev integration staging prod
PROJECTS := $(shell jq -r '.systems[] | .repo' config.json)

default: site

.PHONY: clean
clean:
	git clean -fd

.PHONY: site
site:
	for e in $(ENVIRONMENTS); do \
		mkdir -p environments/$$e; \
		python3 build_index_html.py --environment-filter $$e > environments/$$e/index.html; \
	done
	for p in $(PROJECTS); do \
		mkdir -p projects/$$p; \
		python3 build_index_html.py --project-filter $$p > projects/$$p/index.html; \
	done
