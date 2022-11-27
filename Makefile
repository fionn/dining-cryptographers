MAKEFLAGS = --warn-undefined-variables

SRC = dc.py
TEST = test.py

export PIP_DISABLE_PIP_VERSION_CHECK=1

tags: $(SRC) $(TEST)
	@ctags --languages=python --python-kinds=-i $^

.PHONY: test
test:
	@python -m unittest --buffer

coverage: $(SRC) $(TEST)
	@coverage run --branch --concurrency=thread --omit=venv/* $(TEST)
	@coverage report -m
	@coverage html -d ./coverage
	@coverage erase

.PHONY: lint
lint:
	@pylint -f colorized $(SRC) $(TEST)

.PHONY: flake8
flake8:
	@flake8 $(SRC) $(TEST)

.PHONY: typecheck
typecheck:
	@mypy $(SRC) $(TEST)

.PHONY: clean
clean:
	@$(RM) -r coverage/
	@$(RM) -r .mypy_cache/
	@$(RM) -r __pycache__/
	@$(RM) tags
