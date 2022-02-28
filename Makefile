.PHONY: tests
test:
	pytest tests


.PHONY: publish
publish:
	py -m pip install --upgrade build
	py -m build
	py -m pip install --upgrade twine
	py -m twine upload --repository pypi dist/*
