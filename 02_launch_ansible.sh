#!/usr/bin/env bash

# TODO: src image only if not found
echo '--------------------'
echo '--- Build image ----'
echo '--------------------'
docker src -t raspct_ansible images/ansible

echo '-----------------'
echo '--- Run image ---'
echo '-----------------'

docker run -it -v $(pwd)/ansible:/etc/ansible -v $(pwd)/keys:/home/raspc/.ssh/ raspct_ansible
