
# Archer T2U Ubuntu installer

Installation:

* Python2.7
```
git clone https://github.com/ivannieto/archer-t2u-ubuntu-installer.git && cd archer-t2u-ubuntu-installer/ && python t2u-installer.py
```
* Python3
```
git clone https://github.com/ivannieto/archer-t2u-ubuntu-installer.git && cd archer-t2u-ubuntu-installer/ && python3 t2u-installer.py
```

This script installs the driver mt7610u_wifi_sta_v3002_dpo_20130916 patched by the chenhaiq fork in [driver repository](https://github.com/chenhaiq/mt7610u_wifi_sta_v3002_dpo_20130916).

It works on systems using Ubuntu [<16.10].

For more info configuring the adapter please refer to README_STA_usb from **driver-files** folder. Also reading the README.md included in the same folder will solve some possible runtime errors.

Just follow the instructions from the prompt.

## **Restart your computer when the installation is finished** 

Once you had restarted, you can enable or disable the driver. Plug your USB dongle and run:

```
sudo t2u-driver
```

