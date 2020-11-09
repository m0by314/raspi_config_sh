FROM alpine

RUN apk update && \
    apk add openssh sshpass bash   && \
    adduser -D raspc

USER raspc

COPY ssh_key.sh .

ENTRYPOINT [ "./ssh_key.sh" ]
CMD [ "-h" ]