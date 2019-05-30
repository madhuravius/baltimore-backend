PYTEST := pytest
COVERAGE := --cov=. --cov-config=.coveragerc
PYLINT := pylint ./**/*.py --rcfile=./.pylintrc --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"

lint: 
	$(PYLINT) $(PYTHON_MODULES)
test: 
	$(PYTEST) $(PYTHON_MODULES)
coverage:
	${PYTEST} ${COVERAGE}