#!/usr/bin/env bash

# Download ansible role
ansible-galaxy install m0by314.ansible_raspberry_pi_config

# ansible vault
vault_key_file="/etc/ansible/vault_key_file"
role_vars_file="/etc/ansible/vars/vault.yml"

echo -n Password to encrypt:
read -s password
echo

if [ ! -e $vault_key_file ]; then
  openssl rand -base64 512 | xargs > $vault_key_file
fi

echo >> $role_vars_file
ansible-vault encrypt_string --vault-password-file $vault_key_file $password --name 'rasp_user_password' >> $role_vars_file

# launch playbook
ansible-playbook playbook/config.yml --vault-password-file vault_key_file