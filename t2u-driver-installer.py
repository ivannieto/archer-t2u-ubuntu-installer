import os

PATH = os.getcwd()
HOME = os.getenv('HOME')
INSTALL_FILES = PATH+'/driver-files'
DEV_DIR = HOME+'/test-install'
PROD_DIR = '/etc'
BIN_DIR = '/usr/bin/'

print(('*'*25)+'\n')
print()

def take_input():
    i = input("Please, disconnect all devices you're trying to install and press [I]: ")
    return i

while(take_input()!="i"):
    take_input()
else:
    # Install files
    os.system("cd {} && make clean && make && sudo make install".format(INSTALL_FILES))

    # Check for existing installation dirs
    print(os.path)
    if os.path.isdir(PROD_DIR + '/Wireless'):
        pass
    else:
        os.mkdir(PROD_DIR + '/Wireless/RT2870STA/')
        os.mkdir(PROD_DIR + '/Wireless/RT2870STA/')
        

    # Copy configuration file
    os.system("sudo cp {}/RT2870STA.dat {}/Wireless/RT2870STA/RT2870STA.dat".format(INSTALL_FILES, PROD_DIR))

    # Install driver
    os.system("cd {}/os/linux/ && sudo insmod mt7650u_sta.ko".format(INSTALL_FILES))

    # Script generator for running t2u-driver as a system program
    os.system("sudo cp {0}/t2u-driver {1}/t2u-driver && sudo chmod +x {1}/t2u-driver".format(PATH, BIN_DIR))

    # Restart warning
    print("*"*25+"\n\nYour computer should be restarted now.\nPlease close all running programs and restart manually when you're done.\nAn executable will be installed to enable or disable the adapter.\nJust run in your terminal '$ sudo t2u-driver'.")    


