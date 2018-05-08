# IMPORTANT

## This project is no longer maintained

> Thanks to everyone for your support, issue reports and contributions. Sadly I will discontinue the maintenance of the project. I got rid of this dongle, so I can't test it anymore.
> Feel free to fork, adapt and continue this project to fit your needs.

# Archer T2U Ubuntu installer

Installation:

* You should have python3 installed properly.

## Clone For Ubuntu 17.10 [2.0.0](https://github.com/ivannieto/archer-t2u-ubuntu-installer/tree/2.0.0)
```bash
$ git clone --branch 2.0.0 git@github.com:ivannieto/archer-t2u-ubuntu-installer.git
```

## Clone For Ubuntu 16.04 [1.0.0](https://github.com/ivannieto/archer-t2u-ubuntu-installer/tree/1.0.0)
```bash
$ git clone --branch 1.0.0 git@github.com:ivannieto/archer-t2u-ubuntu-installer.git
```

## Install
```bash
$ cd archer-t2u-ubuntu-installer/ && python3 t2u-driver-installer.py
```

This script installs the driver for Archer T2U USB Wi-Fi adapter patched by:

* [chenhaiq](https://github.com/chenhaiq)
* [mt7610u_wifi_sta_v3002_dpo_20130916](https://github.com/chenhaiq/mt7610u_wifi_sta_v3002_dpo_20130916).

It works on systems using Ubuntu <=17.10.

For more info configuring the adapter please refer to [CONFIGURATION.md](https://github.com/ivannieto/archer-t2u-ubuntu-installer/blob/master/CONFIGURATION.md).

Also reading the [README.md](https://github.com/ivannieto/archer-t2u-ubuntu-installer/blob/master/driver-files/README.md) included in `driver-files` will solve some possible runtime errors.

Just follow the instructions from the prompt.

>
> ## IMPORTANT
> Restart your computer when the installation is done
>

## Usage

Once you had restarted, you can enable or disable the driver. Plug your USB dongle and run:

```bash
$ sudo t2u-driver
```
>
> ## IMPORTANT
> It is also recomended to turn off before detaching the USB dongle.
>

## Uninstall

To uninstall t2u-driver type:

```bash
$ sudo uninstall-t2u-driver
```