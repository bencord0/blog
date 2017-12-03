FROM python:3.6.3 as builder
WORKDIR /app/

COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pip install pipenv && pipenv install --deploy

COPY setup.py /app/
COPY setup.cfg /app/
COPY src /app/src/

RUN python ./setup.py bdist_wheel && pipenv run pip install ./dist/*

FROM python:3.6.3
WORKDIR /app/

COPY --from=builder /app/Pipfile /app/
COPY --from=builder /app/Pipfile.lock /app/
COPY --from=builder /root/.cache /root/.cache
COPY --from=builder /root/.local /root/.local
COPY --from=builder /root/.virtualenvs /root/.virtualenvs
RUN pip install pipenv

RUN pipenv run blog manage collectstatic --noinput

CMD ["pipenv", "run", "blog", "-b", "0.0.0.0:8000"]
