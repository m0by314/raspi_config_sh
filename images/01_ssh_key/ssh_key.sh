#!/usr/bin/env bash

if [ "$1" == "-h" ]; then
  echo "Usage: $0 password user target"
  exit
fi

if [ -e ~/.ssh/id_rsa ]; then
  rm ~/.ssh/*
fi

ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa

sshpass -p "$1" ssh-copy-id -o StrictHostKeyChecking=no "$2"@"$3"