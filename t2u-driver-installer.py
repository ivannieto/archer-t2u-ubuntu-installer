import subprocess as sp
import os

PATH = os.getcwd()
HOME = os.getenv('HOME')
INSTALL_FILES = PATH+'/driver-files'
DEV_DIR = HOME+'/test-install'
PROD_DIR = '/etc'
BIN_DIR = '/usr/bin/'

print('*'*25 +'\n')

def take_input():
    '''
    Takes input from user
    '''
    i = input("Please, disconnect all devices you're trying to install and press [I]: ")
    return i.lower()

def install():
    '''
    Install required files
    '''
    # Install files
    sp.Popen(["cd {} && make clean && make && \
    sudo make install".format(INSTALL_FILES)], shell=True).communicate()

    # Check for existing installation dirs
    sp.Popen(["sudo mkdir {}/Wireless/".format(PROD_DIR)], shell=True).communicate()
    sp.Popen(["sudo mkdir {}/Wireless/RT2870STA/".format(PROD_DIR)], shell=True).communicate()

    # Copy configuration file
    sp.Popen(["sudo cp {0}/RT2870STA.dat \
    {1}/Wireless/RT2870STA/RT2870STA.dat".format(INSTALL_FILES, PROD_DIR)], shell=True).communicate()

    # Install driver module
    sp.Popen(["cd {}/os/linux/ && \
    sudo insmod mt7650u_sta.ko".format(INSTALL_FILES)], shell=True).communicate()

    # Script generator for running t2u-driver as a system program
    sp.Popen(["sudo cp {0}/t2u-driver {1}/t2u-driver && \
    sudo chmod +x {1}/t2u-driver".format(PATH, BIN_DIR)], shell=True).communicate()
    sp.Popen(["sudo cp {0}/uninstall-t2u-driver {1}/uninstall-t2u-driver && \
    sudo chmod +x {1}/uninstall-t2u-driver".format(PATH, BIN_DIR)], shell=True).communicate()

    # Restart warning
    print("*"*25+"\n\n\
    Your computer should be restarted now.\n\
    Please close all running programs and restart manually when you're done.\n\
    An executable will be installed to enable or disable the adapter.\n\
    Just run in your terminal '$ sudo t2u-driver'.")

while(take_input()!="i"):
    continue
else:
    install()
