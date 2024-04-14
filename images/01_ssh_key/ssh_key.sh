#!/usr/bin/env bash

if [ "$1" == "-h" ]; then
  echo "Usage: $0 password user target"
  exit
fi

if [ ! -e ~/.ssh/id_rsa ]; then
  ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa
fi

sshpass -p "$1" ssh-copy-id -f -o StrictHostKeyChecking=no -i ~/.ssh/id_rsa  "$2"@"$3"