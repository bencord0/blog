FROM python:3.6.1

EXPOSE 8000
ENTRYPOINT ["/usr/bin/blog"]
CMD ["-b", "0.0.0.0:8000"]

ADD ./blog.pex /usr/bin/blog

RUN /usr/bin/blog manage collectstatic --noinput
