default: site

.PHONY: clean
clean:
	git clean -fd
	find . | egrep -v '^[.]|[.][.]|[.]/LICENSE[.]txt|[.]/Makefile|[.]/README.md|[.]/nanoc|[.]git$$' | xargs rm -r

.PHONY: site
site:
	cd nanoc && nanoc
	cp -r nanoc/output/* ./

