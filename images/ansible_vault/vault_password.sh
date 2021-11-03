#!/usr/bin/env bash


vault_key_file="/etc/ansible/vault_key_file"
role_vars_file="/etc/ansible/raspbian-config/vars/main.yml"

echo -n Password to encrypt:
read -s password
echo

if [ ! -e $vault_key_file ]; then
  openssl rand -base64 512 | xargs > $vault_key_file
fi

echo >> raspbian-config/vars/main.yml
ansible-vault encrypt_string --vault-password-file $vault_key_file $password --name 'password' >> raspbian-config/vars/main.yml