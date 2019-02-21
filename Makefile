ENVIRONMENTS := dev integration staging prod
PROJECTS := $(shell jq -r '.systems[] | .repo' config.json | sort | uniq)
OWNERS := $(shell jq -r '.systems[] | .owner' config.json | sort | uniq)

default: site

.PHONY: clean
clean:
	rm -rf projects owners environments index.html

.PHONY: site
site:
	for e in $(ENVIRONMENTS); do \
		mkdir -p environments/$$e; \
		python3 build_index_html.py --environment-filter "$$e" > "environments/$$e/index.html"; \
	done
	for p in $(PROJECTS); do \
		mkdir -p projects/$$p; \
		python3 build_index_html.py --project-filter "$$p" > "projects/$$p/index.html"; \
	done
	for o in $(OWNERS); do \
		mkdir -p owners/$$o; \
		python3 build_index_html.py --owner-filter "$$o" > "owners/$$o/index.html"; \
	done
	python3 build_index_html.py > ./index.html; \
