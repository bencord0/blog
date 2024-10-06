FROM node as client
WORKDIR /app/src/client/

COPY src/client /app/src/client/
RUN npm install
RUN npm run build

FROM python as builder
WORKDIR /app/

# From build context
COPY requirements.txt /app/
COPY setup.py /app/
COPY setup.cfg /app/
COPY src /app/src/

# From previous stages
COPY --from=client /app/src/client/build/ /app/src/client/build/

RUN pip install -r requirements.txt
RUN blog manage collectstatic --noinput

CMD ["blog", "-b", "0.0.0.0:8000"]
