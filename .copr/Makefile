srpm:
	spectool -R -g $spec
	rpmbuild -bs $spec
	mv ~/rpmbuild/SRPMS/* $outdir
