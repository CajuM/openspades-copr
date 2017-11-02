srpm:
	dnf install -y rpmdevtools
	cd $(spec)
	mkdir -p ~/rpmbuild/SOURCES
	cp * ~/rpmbuild/SOURCES/
	spectool -R -g openspades.spec
	rpmbuild -bs openspades.spec
	mv ~/rpmbuild/SRPMS/*.rpm $(outdir)
