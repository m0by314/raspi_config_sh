FROM alpine

RUN apk update && \
    apk add ansible bash openssh openssl && \
    adduser -D raspc

USER raspc

WORKDIR /etc/ansible

COPY vault_password.sh /usr/local/bin

CMD ["/bin/bash", "/usr/local/bin/vault_password.sh"]