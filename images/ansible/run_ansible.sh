#!/usr/bin/env bash

# Download ansible role
ansible-galaxy install m0by314.ansible_raspberry_pi_config

# ansible vault
vault_key_file="/etc/ansible/vault_key_file"
vault_vars_file="/etc/ansible/playbook/vars/user_pwd.yml"

# Ask password for the new pi user
i=3
while [ $i -gt 0 ]
do
  echo -n Password for the new user:
  read -s password
  echo

  echo -n Confirm password:
  read -s confirm_password
  echo

  ((i--))
  if [ "$password"x == ""x ] || [ "$password"x != "$confirm_password"x ]; then
      echo "The password confirmation does not match"
      if [ "$i" == 0 ]; then
        exit 1
      fi
  else
    break
  fi
done

# create vault key file
if [ ! -e $vault_key_file ]; then
  openssl rand -base64 512 | xargs > $vault_key_file
fi

# create vault vars file
echo >> $vault_vars_file

# encrypted password to sha512
encrypted_pwd=$(python3 /usr/local/bin/encrypt_password.py "$password")

# write encrypted password into user_pwd.yml
echo "rasp_user_encrypted_password: ${encrypted_pwd}" > $vault_vars_file

# write encrypted vault variable
ansible-vault encrypt_string --vault-password-file $vault_key_file "$password" --name 'rasp_user_password' >> $vault_vars_file


# launch playbook
ansible-playbook playbook/config.yml --vault-password-file vault_key_file -i inventory/hosts.json