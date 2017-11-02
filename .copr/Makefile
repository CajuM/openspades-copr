srpm:
	dnf install -y rpmdevtools
	spectool -R -g $(spec)
	rpmbuild -bs $(spec)
	mv ~/rpmbuild/SRPMS/* $(outdir)
