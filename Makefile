build:
	mkdocs build --clean
	touch docs/.nojekyll

serve:
	mkdocs serve