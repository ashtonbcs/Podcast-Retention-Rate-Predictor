FROM ubuntu:latest
LABEL authors="atown"

ENTRYPOINT ["top", "-b"]