FROM bencord0/python:3.6

ENV LD_LIBRARY_PATH=/usr/lib64/postgresql-9.5/lib64
EXPOSE 8000
ENTRYPOINT ["/usr/bin/blog"]
CMD ["-b", "0.0.0.0:8000"]

ADD ./blog.pex /usr/bin/blog

RUN /usr/bin/blog manage collectstatic --noinput
