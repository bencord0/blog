FROM bencord0/python:3.5.2
ENV PORT=8000
EXPOSE 8000
ENTRYPOINT ["/usr/bin/blog"]

ADD dist /dist
RUN python3.5 -m ensurepip && \
 python3.5 -m pip install --use-wheel /dist/*.whl

USER 1000


