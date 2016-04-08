.PHONY: docs

init:
	pip install -r requirements.txt
	pyxbgen --binding-root=./ebu_tt_live/bindings -m __init__ --schema-root=./ebu_tt_live/xsd/ -r -u ebutt_live.xsd

test:
	pip install -r requirements-test.txt
	py.test tests

docs:
	cd docs && make html