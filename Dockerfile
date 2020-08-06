FROM python:3.8 as builder
WORKDIR /app/

COPY Pipfile /app/
COPY Pipfile.lock /app/
COPY setup.py /app/
COPY setup.cfg /app/
COPY src /app/src/

RUN pip install pipenv && pipenv install --deploy
RUN pipenv run blog manage collectstatic --noinput

CMD ["pipenv", "run", "blog", "-b", "0.0.0.0:8000"]
