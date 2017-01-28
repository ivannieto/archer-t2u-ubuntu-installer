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

    # Comprobar si existe el directorio de destino de la configuracion y si no existe crearlo
    print(os.path)
    if os.path.isdir(DEV_DIR + '/Wireless/RT2870STA/'):
        pass
    else:
        os.mkdir(DEV_DIR + '/Wireless/RT2870STA/')

    # Copiar el archivo de configuracion
    os.system("sudo cp {}/RT2870STA.dat {}/Wireless/RT2870STA/RT2870STA.dat".format(INSTALL_FILES, DEV_DIR))

    # Instalar el modulo del driver
    os.system("cd {}/os/linux/ && sudo insmod mt7650u_sta.ko".format(INSTALL_FILES))

    # Generar el script que debería correrse al inicio del sistema para levantar la conexion
    os.system("sudo cp {0}/t2u-driver {1}/t2u-driver && sudo chmod +x {1}/t2u-driver".format(PATH, BIN_DIR))

    # Avisar de las opciones para deshabilitar o levantar el adaptador desde el programa LOCAL_BIN
    print("*"*25+"\n\nYour computer should be restarted now.\nPlease close all running programs and restart manually when you're done.\nAn executable will be installed to enable or disable the adapter.\nJust run in your terminal '$ sudo t2u-driver'.")    


