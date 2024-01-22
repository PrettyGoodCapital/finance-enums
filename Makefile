tests: ## Clean and Make unit tests
	python3.7 -m pytest -v tests --cov=finance_enums --junitxml=python_junit.xml --cov-report=xml --cov-branch

test: lint ## run the tests for travis CI
	@ python3.7 -m pytest -v tests --cov=finance_enums --junitxml=python_junit.xml --cov-report=xml --cov-branch

lint: ## run linter
	python3.7 -m flake8 finance_enums 

annotate: ## MyPy type annotation check
	mypy -s finance_enums

annotate_l: ## MyPy type annotation check - count only
	mypy -s finance_enums | wc -l 

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf 
	find . -name "*.pyc" | xargs rm -rf 
	rm -rf .coverage cover htmlcov logs build dist *.egg-info
	make -C ./docs clean

docs:  ## make documentation
	make -C ./docs html

install:  ## install to site-packages
	pip3 install .

dist:  ## dist to pypi
	rm -rf dist build
	python3.7 setup.py sdist
	python3.7 setup.py bdist_wheel
	twine check dist/* && twine upload dist/*

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean test tests help annotate annotate_l docs dist
