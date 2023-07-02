.DEFAULT_GOAL := help
.PHONY: help
# Thanks to Francoise at marmelab.com for this
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

OTHER_ARGS :=

.PHONY: develop-py develop-cpp develop-rust develop
develop-py:
	pip install -U toml
	pip install `python -c 'import toml; c = toml.load("pyproject.toml"); print(" ".join(c["project"]["optional-dependencies"]["develop"]))'`

develop-cpp:
	echo "C++ ready"

develop-rust:
	rustup component add rustfmt
	rustup component add clippy
	cargo install cargo2junit
	cargo install grcov
	# cargo install -f wasm-bindgen-cli
	# rustup target add wasm32-unknown-unknown
	# rustup component add llvm-tools-preview

develop: develop-py  ## Setup project for development

.PHONY: build-py build-cpp build-rust build
build-py:
	python setup.py build build_ext --inplace

build-cpp:
	cmake -B build . -DBUILD_PYTHON=Off
	cmake --build build -- -j8

build-rust:
	cargo build --release --all-features --manifest-path=rust/Cargo.toml

build: build-cpp build-py  ## Build the project

.PHONY: lint-py lint-cpp lint-rust lint
lint-py:
	python -m ruff finance_enums

lint-cpp:
	clang-format --dry-run -Werror -i -style=file `find ./src -name "*.*pp"`  || echo "C++ needs reformatting"

lint-rust:
	cargo clippy --all-features --manifest-path=rust/Cargo.toml
	cargo fmt --all  --manifest-path=rust/Cargo.toml -- --check

lint: lint-cpp lint-py  ## Run project linters

.PHONY: fix-py fix-cpp fix-rust fix
fix-py:
	python -m ruff finance_enums --fix

fix-cpp:
	clang-format -i -style=file `find ./src -name "*.*pp"`

fix-rust:
	cargo fmt --all --manifest-path=rust/Cargo.toml

fix: fix-cpp fix-py  ## Run project autofixers

.PHONY: tests-py tests-cpp test-rust tests test tests-ci tests-ci-rust
tests-py:
	python -m pytest -v finance_enums/tests --junitxml=junit.xml --cov=finance_enums --cov-branch --cov-fail-under=65 --cov-report term-missing --cov-report xml

tests-cpp:
	echo "TODO C++ tests"

tests-rust:
	DYLD_LIBRARY_PATH=lib LD_LIBRARY_PATH=lib cargo test --manifest-path=rust/Cargo.toml -- --show-output

tests-ci-rust:
	{ \
		export CARGO_INCREMENTAL=0;\
		export RUSTDOCFLAGS="-Cpanic=abort";\
		export RUSTFLAGS="-Zprofile -Ccodegen-units=1 -Copt-level=0 -Clink-dead-code -Coverflow-checks=off -Zpanic_abort_tests -Cpanic=abort";\
		cargo test --manifest-path=rust/Cargo.toml -- -Z unstable-options --format json | cargo2junit > rust/junit.xml;\
		grcov . --llvm -s . -t cobertura --branch --ignore-not-existing -o ./coverage.xml;\
	}

tests: tests-cpp tests-py  ## Run the tests
test: tests

tests-ci: tests-cpp tests-py

.PHONY: dist-sdist dist-wheel dist-rust dist publish publish-rust

dist-sdist:  ## Create python source dist
	python setup.py sdist

dist-wheel:  ## Create python wheel dist
	python setup.py bdist_wheel $(OTHER_ARGS)

dist-cibw:  ## Create python wheel dist with cibuildwheel
	python -m cibuildwheel --output-dir dist 

dist-rust:
	cargo publish --dry-run --manifest-path=rust/Cargo.toml

dist: build dist-sdist dist-wheel  ## Create python dists
	python -m twine check target/wheels/*

publish: dist  ## Dist assets to pypi
	python -m twine upload target/wheels/* --skip-existing

publish-rust:
	cargo publish --manifest-path=rust/Cargo.toml

clean:  ## Clean the repo
	git clean -fdx
