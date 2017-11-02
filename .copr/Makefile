srpm:
	dnf install -y rpmdevtools
	cd $(spec)
	cp * /builddir/build/SOURCES/
	spectool -R -g openspades.spec
	rpmbuild -bs openspades.spec
	mv /builddir/build/SRPMS/*.rpm $(outdir)
