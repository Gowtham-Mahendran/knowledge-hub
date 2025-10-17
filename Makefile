build:
	mkdocs build --clean
	touch docs/.nojekyll
	echo 'gowt.dev' > docs/CNAME

serve:
	mkdocs serve