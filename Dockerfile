FROM bencord0/python:3.5.2

EXPOSE 8000
ENTRYPOINT ["/usr/bin/blog"]
CMD ["-b", "0.0.0.0:8000"]

ADD ./dist/etc /etc
ADD ./dist/usr/lib64 /usr/lib64
ADD ./blog.pex /usr/bin/blog
