import os

devices = bytearray(os.system("lsusb").decode('utf-8')
for device in devices.split("\n"):
    device.decode('utf-8')
    print("MIO > ", device)
    # print(device)

