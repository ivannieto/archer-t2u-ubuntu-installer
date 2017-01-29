## README

# Ralink Tech Inc.
**[Website](http://www.ralinktech.com)**

Model Name:
====================

**RT2870 Wireless Lan Linux Driver**

Driver Name:
====================

**rt2870.o/rt2870.ko**

Supporting Kernel:
====================

Linux kernel 2.4 and 2.6 series.

**Tested in Redhat 7.3 or later.**


Ralink Hardware:
====================

Ralink 802.11n Wireless LAN Card.

Description:
====================

This is a linux device driver for Ralink RT2870 USB ABGN WLAN Card.

Contents:
====================

* Makefile: Makefile
* *.c: c files
* *.h: header files

Features:
====================
   This driver implements basic IEEE802.11. Infrastructure and adhoc mode with open or shared or WPA-PSK or WPA2-PSK authentication method. 
   NONE, WEP, TKIP and AES encryption. 


Build Instructions:  
====================

`$ tar -xvzf DPB_RT2870_Linux_STA_x.x.x.x.tgz`

`$ cd ./DPB_RT2870_Linux_STA_x.x.x.x`

In **Makefile** set **MODE = STA** and **TARGET = LINUX**

Search `ifeq ($(PLATFORM),PC)` and define the Linux kernel source. Modify to meet your needs.

In `os/linux/config.mk`:

* Define the GCC and LD of the target machine
* Define the compiler flags CFLAGS
* Build for being controlled by NetworkManager or wpa_supplicant wext functions:
	* Set `HAS_WPA_SUPPLICANT=y`
	* Set `HAS_NATIVE_WPA_SUPPLICANT_SUPPORT=y`
	* `cd wpa_supplicant-x.x.x`
	* `./wpa_supplicant -Dwext -ira0 -c wpa_supplicant.conf -d`
* Build for being controlled by WpaSupplicant with Ralink Driver:
	* Set `HAS_WPA_SUPPLICANT=y`
	* Set `HAS_NATIVE_WPA_SUPPLICANT_SUPPORT=n`
	* `cd wpa_supplicant-0.5.7`
	* `./wpa_supplicant -Dralink -ira0 -c wpa_supplicant.conf -d`

Compile the driver source code:

`$ make clean`

`$ make`

**Fix "error: too few arguments to function iwe_stream_add_event"**

`$ patch -i os/linux/sta_ioctl.c.patch os/linux/sta_ioctl.c`

`$ sudo cp RT2870STA.dat  /etc/Wireless/RT2870STA/RT2870STA.dat`

## Load the driver from `./os/linux` directory.

* *[kernel 2.4]*

	`$/sbin/insmod rt2870sta.o`

	`$/sbin/ifconfig ra0 inet YOUR_IP up`

* *[kernel 2.6]*

	`$/sbin/insmod rt2870sta.ko`

	`$/sbin/ifconfig ra0 inet YOUR_IP up`

## Unload driver
	`$/sbin/ifconfig ra0 down`

	`$/sbin/rmmod rt2870sta`

# Configuration

RT2870 driver can be configured via following interfaces:

* `iwconfig` command
* `iwpriv` command
* configuration file

`iwconfig` comes with kernel. For `iwpriv` usage and details, please refer to file `iwpriv_usage.txt`.

Modify configuration file `RT2870STA.dat` in `/etc/Wireless/RT2870STA/RT2870STA.dat`.

# Configuration File: RT2870STA.dat

Copy this file to /etc/Wireless/RT2870STA/RT2870STA.dat

This file is a binary file and will be read on loading rt.o module.

Use any text editor to modify settings according to your need.

[1]&emsp;**Set NetworkType** to `Adhoc` for using Adhoc-mode, otherwise use `Infra`

[2]&emsp;**Set Channel** to `0` for auto-select on Infrastructure mode

[3]&emsp;**Set SSID** for connecting to your Access-point.

[4]&emsp;**AuthMode** can be:
	* WEPAUTO
	* OPEN
	* SHARED
	* WPAPSK
	* WPA2PSK
	* WPANONE

[5]&emsp;**EncrypType** can be:
	* NONE
	* WEP
	* TKIP
	* AES

For more information refer to the README file.


Example:

```
#The word of "Default" must not be removed
Default
CountryRegion=5
CountryRegionABand=7
CountryCode=
SSID=Dennis2860AP
NetworkType=Infra
WirelessMode=9
Channel=0
BeaconPeriod=100
TxPower=100
BGProtection=0
TxPreamble=0
RTSThreshold=2347
FragThreshold=2346
TxBurst=1
WmmCapable=0
AckPolicy=0;0;0;0
AuthMode=OPEN
EncrypType=NONE
WPAPSK=
DefaultKeyID=1
Key1Type=0
Key1Str=
Key2Type=0
Key2Str=
Key3Type=0
Key3Str=
Key4Type=0
Key4Str=
PSMode=CAM
FastRoaming=0
RoamThreshold=70
HT_RDG=1
HT_EXTCHA=0
HT_OpMode=1
HT_MpduDensity=4
HT_BW=1
HT_AutoBA=1
HT_BADecline=0
HT_AMSDU=0
HT_BAWinSize=64
HT_GI=1
HT_MCS=33
HT_MIMOPSMode=3
EthConvertMode=
EthCloneMac=
IEEE80211H=0
TGnWifiTest=0
WirelessEvent=0
MeshId=MESH
MeshAutoLink=1
MeshAuthMode=OPEN
MeshEncrypType=NONE
MeshWPAKEY=
MeshDefaultkey=1
MeshWEPKEY=
CarrierDetect=0
```

-----------------------------------------------
### NOTE:

WMM parameters:
	* **WmmCapable**&emsp;Set it as 1 to turn on WMM Qos support
	* **AckPolicy1~4**&emsp;Ack policy which support normal Ack or no Ack (AC_BK, AC_BE, AC_VI, AC_VO)

All **WMM parameters do not support iwpriv** command **but WmmCapable**, please store all parameter to RT2870STA.dat, and restart driver.

-----------------------------------------------

#### Syntax is: 'Param'='Value' and describes below. 

* ### CountryRegion=value

	| Value  | Description |
	|---|---|
	| 0 | use 1 ~ 11 Channel |
	| 1 | use 1 ~ 13 Channel |
	| 2 | use 10 ~ 11 Channel |
	| 3 | use 10 ~ 13 Channel |
	| 4 | use 14 Channel |
	| 5 | use 1 ~ 14 Channel |
	| 6 | use 3 ~ 9 Channel |
	| 7 | use 5 ~ 13 Channel |
	| 31 | use 1 ~ 14 Channel (ch1-11:active scan, ch12-14 passive scan) |

   	 	                                      
* ### CountryRegionABand=value      							

	| Value  | Description |
	|---|---|
	| 0 | use 36, 40, 44, 48, 52, 56, 60, 64, 149, 153, 157, 161, 165 Channel |
	| 1 | use 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140 Channel |
	| 2 | use 36, 40, 44, 48, 52, 56, 60, 64 Channel |
	| 3 | use 52, 56, 60, 64, 149, 153, 157, 161 Channel |
	| 4 | use 149, 153, 157, 161, 165 Channel |
	| 5 | use 149, 153, 157, 161 Channel |
	| 6 | use 36, 40, 44, 48 Channel |
	| 7 | use 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165 Channel |
	| 8 | use 52, 56, 60, 64 Channel |
	| 6 | use 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 132, 136, 140, 149, 153, 157, 161, 165 Channel |
	| 9 | use 36, 40, 44, 48, 149, 153, 157, 161, 165 Channel |
	| 10 | use 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 149, 153, 157, 161 Channel |
	| 11 | use 52, 56, 60, 64 Channel |

* ### CountryCode=value

	AG, AR, AW, AU, AT, BS, BB, BM, BR, BE, BG, CA, KY, CL, CN, CO, CR, CY, CZ, DK, DO, EC, SV, FI, FR, DE, GR, GU, GT, HT, HN, HK, HU, IS, IN, ID, IE, IL, IT, JP, JO, LV, LI, LT, LU, MY, MT, MA, MX, NL, NZ, NO, PE, PT, PL, RO, RU, SA, CS, SG, SK, SI, ZA, KR, ES, SE, CH, TW, TR, GB, UA, AE, US, VE

	**Default Settings:**

	[0]&emsp;2.4 G - ch 1~11

	[10]&emsp;5G - ch 52~64, 100~140, 149~165

* ### SSID=value

	**0~z, 1~32 ascii characters.**

* ### WirelessMode=value
	| Value  | Description |
	|---|---|
	| 0 | legacy 11b/g mixed  |
	| 1 | legacy 11B only |
	| 2 | legacy 11A only ***Not support in RfIcType=1(id=RFIC_5225) and RfIcType=2(id=RFIC_5325)*** |
	| 3 | legacy 11a/b/g mixed ***Not support in RfIcType=1(id=RFIC_5225) and RfIcType=2(id=RFIC_5325)*** |
	| 4 | legacy 11G only |
	| 5 | 11ABGN mixed |
	| 6 | 11N only |
	| 7 | 11GN mixed |
	| 8 | 11AN mixed |
	| 9 | 11BGN mixed |
	| 10 | 11AGN mixed |
    
* ### Channel=value
	Depends on CountryRegion or CountryRegionABand
                    	
* ### BGProtection=value
	| Value  | Description |
	|---|---|
	| 0 | Auto |
	| 1 | Always on  |
	| 2 | Always off |

                    	
* ### TxPreamble=value
	| Value  | Description |
	|---|---|
	| 0 | Preamble Long |
	| 1 | Preamble Short  |
	| 2 | Auto |  

* ### RTSThreshold=value
	`1~2347`

* ### FragThreshold=value
	`256~2346`
	
* ### TxBurst=value
	| Value  | Description |
	|---|---|
	| 0 | Disable |
	| 1 | Enable  |

* ### NetworkType=value
	| Value  | Description |
	|---|---|
	| Infra | infrastructure mode |
	| Adhoc | adhoc mode  |


* ### AuthMode=value

	| Value  | Description |
	|---|---|
	| OPEN | For open system	 |
	| SHARED | For shared key system  |
	| WEPAUTO | Auto switch between OPEN and SHARED |
	| WPAPSK  | For WPA pre-shared key  (Infra)  |
	| WPA2PSK  | For WPA2 pre-shared key (Infra) |
	| WPANONE | For WPA pre-shared key  (Adhoc)  |
	| WPA | Use WPA-Supplicant |
	| WPA2 | Use WPA-Supplicant  |


* ### EncrypType=value

	| Value | Description |
	| --- | --- |
	| NONE | For AuthMode=OPEN |
	| WEP | For AuthMode=OPEN or AuthMode=SHARED |
	| TKIP | For AuthMode=WPAPSK or WPA2PSK |
	| AES | For AuthMode=WPAPSK or WPA2PSK |


* ### DefaultKeyID=value
	`1~4`

* ### Key1=value
* ### Key2=value
* ### Key3=value
* ### Key4=value
	Values:
	* 10 or 26 hexadecimal characters eg: 012345678
    * 5 or 13 ascii characters eg: passd
    
	(usage : `iwpriv` only)     

* ### Key1Type=value
* ### Key2Type=value
* ### Key3Type=value
* ### Key4Type=value
	Values:
	* 0   hexadecimal type
	* 1   assic type

    (usage : reading profile only)

* ### Key1Str=value
* ### Key2Str=value
* ### Key3Str=value
* ### Key4Str=value
	Values:
	* 10 or 26 characters (key type=0)
	* 5 or 13 characters  (key type=1)
    
		(usage : reading profile only)	

* ### WPAPSK=value

	| Value | Description |
	| --- | --- |
	| 8~63 | ASCII |
	| 64 | HEX characters |


* ### WmmCapable=value

	| Value | Description |
	| --- | --- |
	| 0 | Disable WMM |
	| 1 | Enable WMM |

* ### PSMode=value

	| Value | Description |
	| --- | --- |
	| CAM | Constantly Awake Mode |
	| Max_PSP | Max Power Savings |
	| Fast_PSP | Power Save Mode |

* ### FastRoaming=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### RoamThreshold=value

	`Positive Integer(dBm)`

* ### HT_RDG=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |


* ### HT_EXTCHA=value (Extended Channel Switch Announcement)

	| Value | Description |
	| --- | --- |
	| 0 | Below |
	| 1 | Above |


* ### HT_OpMode=value

	| Value | Description |
	| --- | --- |
	| 0 | HT mixed format |
	| 1 | HT greenfield formatEnabled |


* ### HT_MpduDensity=value
	**Based on 802.11n D2.0**

	| Value | Description |
	| --- | --- |
	| 0 | no restriction |
	| 1 | 1/4 �gs |
	| 2 | 1/2 �gs |
	| 3 | 1 �gs |
	| 4 | 2 �gs |
	| 5 | 4 �gs |
	| 6 | 8 �gs |
	| 7 | 16 �gs |

* ### HT_BW=value
	| Value | Description |
	| --- | --- |
	| 0 | 20MHz |
	| 1 | 40MHz |

* ### HT_AutoBA=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### HT_BADecline

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled <Reject BA request from AP> |

* ### HT_AMSDU=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### HT_BAWinSize=value

		1 ~ 64

* ### HT_GI=value

		0				long GI
		1				short GI

* ### HT_MCS=value

		0 ~ 15
		33: auto

* ### HT_MIMOPSMode=value
 (based on 802.11n D2.0)
		0				Static SM Power Save Mode
		1				Dynamic SM Power Save Mode
		2				Reserved
		3				SM enabled
	(not fully support yet)

* ### EthConvertMode=value

	* dongle
	* clone
	* hybrid

* ### EthCloneMac=value

	`xx:xx:xx:xx:xx:xx`

* ### IEEE80211H=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### TGnWifiTest=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### WirelessEvent=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled <send custom wireless event> |
	    
* ### MeshId=value

	`Length 1~32 ascii characters`

* ### MeshAutoLink=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

* ### MeshAuthMode=value

	| Value | Description |
	| --- | --- |
	| OPEN | For open system |
	| WPANONE | For WPA pre-shared key  (Adhoc) |


* ### MeshEncrypType=value

	| Value | Description |
	| --- | --- |
	| NONE | For MeshAuthMode=OPEN |
	| WEP | For MeshAuthMode=OPEN |
	| TKIP | For MeshAuthMode=WPANONE |
	| AES | For MeshAuthMode=WPANONE |


* ### MeshWPAKEY=value

	`8~63 ASCII` or `64 HEX characters`

* ### MeshDefaultkey=value

	`1~4`

* ### MeshWEPKEY=value

	`10 or 26 characters`
	`5 or 13 characters`

* ### CarrierDetect=value

	| Value | Description |
	| --- | --- |
	| 0 | Disabled |
	| 1 | Enabled |

MORE INFORMATION
=============

If you want for rt2870 driver to auto-load at boot time:

## AutoLoad at BootTime

* Choose ra0 as first RT2870 WLAN card, ra1 for the second RT2870 WLAN card, etc.

* Create/Edit `ifconfig-ra0` file in `/etc/sysconfig/network-scripts/`, search for the line `alias ra0 xxxx` and add/edit:

	`alias ra0 rt2870sta`
* Create/Edit these lines in the file `/etc/sysconfig/network-scripts/ifcfg-ra0`:

	* DEVICE='ra0'
	* ONBOOT='yes'
	* **For DHCP use add**:
		BOOTPROTO='dhcp'

* To ease the Default Gateway setting, add in `/etc/sysconfig/network`:
	* GATEWAY=x.x.x.x

Dongle/Clone Features:
======================

## Dongle mode

Provides a 1-to-N MAC address mapping mechanism such that more than one PC behind the STA can transparently connect to the AP.

## Clone mode

Provides a 1-to-1 MAC address mapping mechanism. STA can use own MAC as SA MAC or use user desired MAC as SA MAC or use source MAC of first packet coming from wired device as SA MAC.

**NOTE**: In this mode, only the PC who own the specified MAC can connect to the AP.

## Hybrid mode(Dongle+Clone):

Provides a 1-to-N MAC address mapping mechanism such that more than one PC behind the STA can transparently connect to the AP.STA can use own MAC as SA MAC or use user desired MAC as SA MAC or use source MAC of first packet coming from wired device as SA MAC.

**Please refer to "Config STA to link as dongle mode..." in iwpriv_usage.txt for related commands.**