#!/usr/bin/env bash
#####################
# Allows the generation of an ssh key and the copy of it on the target
#
# The generation of the key and the sending is done in a docker container
#
# SSH keys are accessible in the keys folder
#
#
# Mandatory Options:
#    -t | --target   address of the host on which the key must be copied
#
# Options:
#    -u | --user       user to connect by ssh (DEFAULT user is pi)
#    -p | --password   user password (DEFAULT password is raspberry)
#    -h | --help       show help
#
#######################


usage() {
  echo "Usage: $0 -t | --target <IP_address>  [ -u | --user < default pi > ] [ -p | --password < default raspberry > ] [ -h | --help ]"
  echo "           -t | --target     address of the host on which the key must be copied"
  echo "           -u | --user       user to connect by ssh"
  echo "           -p | --password   user password"
  echo "           -h | --help       show help"
}


user="pi"
pwd="raspberry"

while test -n "$1"; do
    case "$1" in

      -u| --user)
        user=$2
        shift 2
        ;;

      -p | --password)
        pwd=$2
        shift 2
        ;;

      -t | --target)
        target=$2
        shift 2
        ;;

      -h | --help)
        usage
        exit 0
        ;;

      * )
        echo "Unimplemented option: $1" >&2
        usage
        exit 1
        ;;

    esac
done

echo '--------------------'
echo '--- Build image ----'
echo '--------------------'
docker build -t raspc_ssh_key images/01_ssh_key

echo '-----------------'
echo '--- Run image ---'
echo '-----------------'
docker run -v ${HOME}/.ssh/:/home/raspc/.ssh/ raspc_ssh_key "$pwd" "$user" "$target"

echo '--------------------'
echo '--- Delete image ---'
echo '--------------------'
docker rmi -f raspc_ssh_key
