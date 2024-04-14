# Scripts to configurate an Raspberry

Set of 3 scripts to facilitate the configuration of a Raspberry
**(Functional with OS Raspbian Lite on MacOS)**

## Prerequisites

 * Docker
 * A Raspbian SD card ([Raspberry Pi Imager](https://www.raspberrypi.org/downloads/) to configure it quickly)
 * If you work MacOS, you need a utility to read partition in ext4 format 

## Usage

#### Script 0: Activate the ssh and assigned a static IP

You must fill in the config.ini file with your data
```bash
# wpa_supplicant.conf
# necessary if you want to configure wifi
#
RASPCT_country="Your country"
RASPCT_ssid="connection name"
RASPCT_psk="wifi code"


# dhcpcd.conf
#
RASPCT_ip_address=<Ip address ex: 192.168.1.15>
RASPCT_routers=<routers ip>
RASPCT_domain_name_servers="dns ip  ex: 192.168.1.1 8.8.8.8"
```

Then run the script `00_pre_boot_.sh`  
  
    
*For these example the boot partition of the SD card is mounted on /Volumes/boot and the system partition /Volumes/rootfs*
* __Example for activated WiFi__: 
``` bash
./00_pre_boot.sh -b /Volumes/boot -s /Volumes/rootfs -w 
```
* __Example for activated Ethernet__:
``` bash
./00_pre_boot.sh -b /Volumes/boot -s /Volumes/rootfs 
```


#### Script 1: Generate an ssh key to allow a connection with the ansible server:
```bash
./01_ssh_key.sh -t <Raspberry IP>
```
This script uses the default credentials to connect to the raspberry  
*It is possible to change the  default credentials by using the options -u < user > and -p < password >*

#### Script 2: Configuring raspberry with ansible

```bash
./02_launch_ansible.sh
```
This script launches a playbook named config.yml (found in `ansible/playbook/config.yml`).  
The host file is located in `ansible/inventory/hosts.json`, default value:
- "ansible_host": "raspberrypi"
- "ansible_port": 22
- "ansible_user": "pi"

The playbook uses a configuration role which allows:
- creating a new user and deleting the "pi" account
- change ssh port
- activate or deactivate the raspberry I/O (serial, camera, vnc, spi, i2c etc ...)
- install packages
- activate the firewall
- open ports

[For more details on the role variable](https://galaxy.ansible.com/ui/standalone/roles/m0by314/ansible_raspberry_pi_config/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
