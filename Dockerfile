FROM python:3.6.2 as builder

ENV WHEELHOUSE=/wheelhouse
ENV PIP_WHEEL_DIR=/wheelhouse
ENV PIP_FIND_LINKS=/wheelhouse

COPY requirements.txt /app/requirements.txt
RUN pip wheel -r /app/requirements.txt

COPY setup.py /app
COPY setup.cfg /app
COPY src /app/
RUN pip wheel /app

FROM python:3.6.2

VOLUME /wheelhouse
COPY --from=builder /wheelhouse /wheelhouse

RUN pip install --no-index -f /wheelhouse blog
RUN /usr/local/bin/blog manage collectstatic --noinput

ENTRYPOINT ["/usr/local/bin/blog"]
CMD ["-b", "0.0.0.0:8000"]
