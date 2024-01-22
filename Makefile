tests: ## Clean and Make unit tests
	python -m pytest -v finance_enums/tests --cov=finance_enums --junitxml=python_junit.xml --cov-report=xml --cov-branch

lint: ## run linter
	python -m flake8 finance_enums setup.py 

fix: ## run black
	python -m black finance_enums setup.py

checks: ## run check-manifest
	check-manifest -v

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf 
	find . -name "*.pyc" | xargs rm -rf 
	rm -rf .coverage cover htmlcov logs build dist *.egg-info
	make -C ./docs clean

docs:  ## make documentation
	make -C ./docs html

install:  ## install to site-packages
	python -m pip install .

dist:  ## create dists
	rm -rf dist build
	python setup.py sdist bdist_wheel
	python -m twine check dist/*
	
publish: dist  ## dist to pypi
	python -m twine upload dist/* --skip-existing

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: tests lint checks fix clean docs install dist publish help
