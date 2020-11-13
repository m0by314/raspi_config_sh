# Raspberry configuration tool (RASPCT)

RASPCT is a utility to configure and secure a raspberry without screen or keyboard

TODO: 
   * add role description 
## Prerequisites

 * Docker
 * A Raspbian SD card ([Raspberry Pi Imager](https://www.raspberrypi.org/downloads/) to configure it quickly)

## Usage

#### Step 1: Activate the ssh and assigned a static IP

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
RASPCT_ip_address=<Ip address/mask ex: 192.168.1.15/24>
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
./00_pre_boot.sh -b /Volumes/boot -s /Volumes/rootfs -e 
```
*If the 2 options -w -e are passed to the script, the Ethernet connection takes over and the WiFi connection is not configured*

#### Step 2: Generate an ssh key to allow a connection with the ansible server:
```bash
./01_ssh_key.sh -t <Raspberry IP>
```
The script uses the default credentials to connect to the raspberry  
*It is possible to change the  default credentials by using the options -u < user > and -p < password >*

#### Step 3: Configuring raspberry with ansible
 
 TODO



## License
[MIT](https://choosealicense.com/licenses/mit/)
