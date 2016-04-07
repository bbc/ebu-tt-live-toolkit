.PHONY: docs

init:
	pip install -r requirements.txt

test:
	py.test tests

docs:
	cd docs && make html