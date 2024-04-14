#!/usr/bin/env bash

# TODO: build image only if not found
echo '--------------------'
echo '--- Build image ----'
echo '--------------------'
docker build -t raspct_ansible images/ansible

echo '-----------------'
echo '--- Run image ---'
echo '-----------------'

docker run -it -v $(pwd)/ansible:/etc/ansible -v ${HOME}/.ssh:/home/raspc/.ssh/ raspct_ansible
