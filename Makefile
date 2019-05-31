PYTEST := pytest
COVERAGE := --cov=. --cov-config=.coveragerc
PYLINT := pylint ./**/*.py --rcfile=./.pylintrc --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"

lint: 
	$(PYLINT) $(PYTHON_MODULES)
test: 
	$(PYTEST) $(PYTHON_MODULES)
coverage:
	${PYTEST} ${COVERAGE}
docker-build:
	docker build -t madhuravius/baltimore-backend .
docker-lint:
	docker run \
		-e POSTGRES_URL="not-empty" \
		-e SECRET_KEY="TEST_SECRET" \
		-e ENVIRON="TEST" \
		madhuravius/baltimore-backend make lint
docker-coverage:
	docker run \
		-e POSTGRES_URL="not-empty" \
		-e SECRET_KEY="TEST_SECRET" \
		-e ENVIRON="TEST" \
		madhuravius/baltimore-backend make coverage
docker-test:
	docker run \
		-e POSTGRES_URL="not-empty" \
		-e SECRET_KEY="TEST_SECRET" \
		-e ENVIRON="TEST" \
		madhuravius/baltimore-backend make test
docker-local:
	docker run \
		-e POSTGRES_URL="${LOCAL_POSTGRES_URL}" \
		-e SECRET_KEY="${LOCAL_SECRET_KEY}" \
		-e ENVIRON="LOCAL" \
		-p 8000:8000 \
		madhuravius/baltimore-backend python3 manage.py runserver 0.0.0.0:8000
docker-local-bash:
	docker run \
		-e POSTGRES_URL="${LOCAL_POSTGRES_URL}" \
		-e SECRET_KEY="${LOCAL_SECRET_KEY}" \
		-e ENVIRON="LOCAL" \
		-p 8000:8000 \
		-it \
		madhuravius/baltimore-backend /bin/bash
docker-notebook:
	docker run \
		-e POSTGRES_URL="${LOCAL_POSTGRES_URL}" \
		-e SECRET_KEY="${LOCAL_SECRET_KEY}" \
		-e ENVIRON="LOCAL" \
		-p 8888:8888 \
		madhuravius/baltimore-backend python3 manage.py shell_plus --notebook
docker-make-migrations-local:
	docker run \
		-e POSTGRES_URL="${LOCAL_POSTGRES_URL}" \
		-e SECRET_KEY="${LOCAL_SECRET_KEY}" \
		-e ENVIRON="LOCAL" \
		madhuravius/baltimore-backend python3 manage.py makemigrations
docker-migrate-local:
	docker run \
		-e POSTGRES_URL="${LOCAL_POSTGRES_URL}" \
		-e SECRET_KEY="${LOCAL_SECRET_KEY}" \
		-e ENVIRON="LOCAL" \
		madhuravius/baltimore-backend python3 manage.py migrate
