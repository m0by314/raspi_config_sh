FROM alpine

RUN apk update && \
    apk add ansible bash openssh openssl && \
    adduser -D raspc

USER raspc

WORKDIR /etc/ansible


CMD ["sh", "-c", "tail -f /dev/null"]
