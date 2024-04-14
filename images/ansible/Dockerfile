FROM alpine

RUN apk update && \
    apk add ansible bash openssh openssl python3 py3-pip py3-passlib && \
    adduser -D raspc

USER raspc

WORKDIR /etc/ansible

COPY run_ansible.sh /usr/local/bin
COPY encrypt_password.py /usr/local/bin

CMD ["/bin/bash", "/usr/local/bin/run_ansible.sh"]

#CMD ["sh", "-c", "tail -f /dev/null"]
#CMD ["/bin/bash"]