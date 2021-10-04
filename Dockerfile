FROM node as client
WORKDIR /app/src/client/

COPY src/client /app/src/client/
RUN npm install
RUN npm run build

FROM python:3.10.0b4 as builder
WORKDIR /app/

# From build context
COPY Pipfile /app/
COPY Pipfile.lock /app/
COPY setup.py /app/
COPY setup.cfg /app/
COPY src /app/src/

# From previous stages
COPY --from=client /app/src/client/build/ /app/src/client/build/

RUN pip install pipenv && pipenv install --deploy
RUN pipenv run blog manage collectstatic --noinput

CMD ["pipenv", "run", "blog", "-b", "0.0.0.0:8000"]
