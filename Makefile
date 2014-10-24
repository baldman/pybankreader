.PHONY: clean-pyc test tox-test docs

all: clean-pyc test

test:
	py.test tests

tox-test:
	tox

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

docs:
	$(MAKE) -C docs html