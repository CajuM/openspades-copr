srpm:
	dnf install -y rpmdevtools
	cd $(spec)
	spectool -R -g openspades.spec
	rpmbuild -bs openspades.spec
	mv ~/rpmbuild/SRPMS/* $(outdir)
