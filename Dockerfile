FROM python:3.6.1 as builder
COPY . /source
RUN pip install -r /source/build-requirements.txt
RUN pex -vv -o /usr/bin/blog --disable-cache /source -m blog

FROM python:3.6.1
EXPOSE 8000
ENTRYPOINT ["/usr/bin/blog"]
CMD ["-b", "0.0.0.0:8000"]
COPY --from=builder /usr/bin/blog /usr/bin/blog
RUN /usr/bin/blog manage collectstatic --noinput
