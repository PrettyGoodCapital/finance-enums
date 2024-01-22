tests: ## Clean and Make unit tests
	python3 -m nose -v tests --with-coverage --cover-erase --cover-package=`find finance_enums -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/\.py//g" | tr '\n' ',' | rev | cut -c2- | rev`

test: ## run the tests for travis CI
	@ python3 -m nose -v tests -I 'test_api.py' --with-coverage --cover-erase --cover-package=`find finance_enums -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/\.py//g" | tr '\n' ',' | rev | cut -c2- | rev`

testall: ## run the tests including those that hit the actual api
	@ python3 -m nose -v tests --with-coverage --cover-erase --cover-package=`find finance_enums -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/\.py//g" | tr '\n' ',' | rev | cut -c2- | rev`

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
	python3 setup.py install

dist:  ## dist to pypi
	python3 setup.py sdist upload -r pypi

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean test tests help annotate annotate_l docs dist
