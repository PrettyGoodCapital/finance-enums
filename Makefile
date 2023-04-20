#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python -m pip install -e .[develop]

build-py:  ## build the python library
	python setup.py build build_ext --inplace

build: build-py  ## build the library

install:  ## install library
	python -m pip install .

#########
# LINTS #
#########
lint-py:  ## run python linter with flake8 and black
	python -m ruff finance_enums setup.py
	python -m black --check finance_enums setup.py

lint: lint-py  ## run all lints

# Alias
lints: lint

fix-py:  ## fix python formatting with black
	python -m black finance_enums/ setup.py
	python -m ruff finance_enums/ setup.py --fix

fix: fix-py  ## run all autofixers

# alias
format: fix

################
# Other Checks #
################
check-manifest:  ## check python sdist manifest with check-manifest
	check-manifest -v

checks: check-manifest

# Alias
check: checks

#########
# TESTS #
#########
test:  ## run python tests
	python -m pytest -v finance_enums/tests --junitxml=junit.xml

coverage:  ## run tests and collect test coverage
	python -m pytest -v finance_enums/tests --junitxml=junit.xml --cov=finance_enums --cov-branch --cov-fail-under=80 --cov-report term-missing

# Alias
tests: test

###########
# VERSION #
###########
show-version:  ## show current library version
	bump2version --dry-run --allow-dirty setup.py --list | grep current | awk -F= '{print $2}'

patch:  ## bump a patch version
	bump2version patch

minor:  ## bump a minor version
	bump2version minor

major:  ## bump a major version
	bump2version major

########
# DIST #
########
dist-py:  # build python dists
	python setup.py sdist bdist_wheel

dist-check:  ## run python dist checker with twine
	python -m twine check dist/*
dist: clean build dist-py dist-check  ## build all dists

publish-py:  # publish python assets
	python -m twine upload dist/* --skip-existing
publish: dist publish-py  ## publish all dists

#########
# CLEAN #
#########
deep-clean: ## clean everything from the repository
	git clean -fdx

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info

############################################################################################

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: develop build-py build-js build build install serverextension labextension lint-py lint-js lint-cpp lint lints fix-py fix-js fix-cpp fix format check-manifest checks check annotate semgrep test-py test-js coverage-py show-coverage test tests docs show-docs show-version patch minor major dist-py dist-py-sdist dist-py-local-wheel dist-check dist publish-py publish-js publish deep-clean clean help 
