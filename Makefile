project_name = engine-reports-config-passwd
version = $(shell grep "Version" $(project_name).spec  | awk '{print $$2}')

sources:
	git archive --format=tar --prefix=$(project_name)-$(version)/ HEAD | gzip -9v > $(project_name)-$(version).tar.gz
