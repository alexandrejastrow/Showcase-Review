FROM python:3.10 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

WORKDIR /showcase-review

COPY --from=requirements-stage /tmp/requirements.txt /showcase-review/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /showcase-review/requirements.txt

COPY ./showcase-review /showcase-review/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]