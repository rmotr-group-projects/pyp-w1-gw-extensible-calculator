.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests

test-operations:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests/test_operations.py
	
test-main:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests/test_main.py

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=calculator tests

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=calculator $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report
