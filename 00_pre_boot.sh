#!/usr/bin/env bash
#####################
# Configure the files needed to start a raspberry without keyboard and screen
# Create a ssh file and wpa_supplicant.conf if the wifi option is activated in the boot partition
# Ip static is configured in dhcpcd.conf in the system partition
#
#
# For the script to work, you need to configure the config.ini file:
#
# wpa_supplicant.conf
# necessary if you want to configure wifi
#
# RASPCT_country="Your country"
# RASPCT_ssid="connection name"
# RASPCT_psk="wifi code"
#
#
# dhcpcd.conf
#
# RASPCT_ip_address=<Ip address/mask ex: 192.168.1.15/24>
# RASPCT_routers=<routers ip>
# RASPCT_domain_name_servers="dns ip  ex: 192.168.1.1 8.8.8.8"
#
#######################

usage() {
  echo "Usage: $0 -b <boot partition>  -s <system partition> [-ewh]"
  echo "           -b boot partition on SD Card"
  echo "           -s system partition on SD Card"
  echo "           -w active WiFi with static IP"
  echo "           -h show help"
}

check_path () {
  path=$1

  if [ "$path"x == ""x ] || [ ! -d "$path" ]; then
    echo "Path \"$path\" on SD Card directory is missing or invalid" >&2
    exit
  fi
}

while getopts ':b:s:wh' option
do
  case "${option}"
  in
    b )
       boot_partition=${OPTARG}
       check_path $boot_partition
      ;;
    s )
       sys_partition=${OPTARG}
       check_path $sys_partition
      ;;
    w )
      wifi=true
      ;;
    h )
      usage
      exit
      ;;
    \? )
      echo "Unknown option: -$OPTARG" >&2
      exit 1
      ;;
    : )
      echo echo "Missing option argument for -$OPTARG" >&2
      exit 1
      ;;
    * )
      echo "Unimplemented option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

if [ ! "$boot_partition" ] || [ ! "$sys_partition" ]; then
  echo "arguments -b and -s must be provided"
  usage; exit 1
fi

# File
wpa_supplicant_file="${boot_partition}/wpa_supplicant.conf"
dhcpcd_file="${sys_partition}/etc/dhcpcd.conf"

# source config.ini
echo "Source config.ini"
if [ -e config.ini ]; then
  source config.ini
else
  echo "ERROR: Configuration file "config.ini" is missing"
  exit 1
fi
echo "done"

# Boot section
echo -e "\nBoot section configuration"

echo >> ${boot_partition}/ssh.txt # requires one bit

if $wifi; then
  interface=$RASPCT_wifi_interface
 echo "country=${RASPCT_country}
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid=\"${RASPCT_ssid}\"
 psk=\"${RASPCT_psk}\"
}" > $wpa_supplicant_file
else
  interface=$RASPCT_eth_interface
fi
echo "done"

# IP static
echo -e "\nConfigure the IP static"

if [ ! "$interface"x == ""x  ]; then
  if grep -q "#RASPC config" $dhcpcd_file ; then
    sed -i '' "s#^interface.*#interface ${interface}#
               s#^static ip_address=.*#static ip_address=${RASPCT_ip_address}#
               s#^static routers=.*#static routers=${RASPCT_routers}#
               s#^static domain_name_servers=.*#static domain_name_servers=${RASPCT_domain_name_servers}#" $dhcpcd_file
  else
    echo "
#RASPC config
interface ${interface}
static ip_address=${RASPCT_ip_address}
static routers=${RASPCT_routers}
static domain_name_servers=${RASPCT_domain_name_servers}" >> "$dhcpcd_file"
  fi
fi
echo "done"

# Ansible hosts file
echo -e "\nConfigure Ansible hosts file"

ansible_hosts_file="./ansible/hosts"
if ! grep -q "$RASPCT_ip_address" "$ansible_hosts_file" ; then
  echo "$RASPCT_ip_address" >> "./ansible/hosts"
fi
echo "done"

echo -e "\nYou can put the sd card in the raspberry and start it before launch 01_copy_ssh_key.sh"