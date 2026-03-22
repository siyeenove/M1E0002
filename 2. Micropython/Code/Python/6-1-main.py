# Imports go at the top
from microbit import *

# Car I2C address 
i2cAddr = 0x29

# Firmware version register
ver = bytearray([0x00])

# Initialize the I2C communication interface
i2c.init()


# Code in a 'while True:' loop repeats forever
while True:
    # Read the firmware version
    i2c.write(i2cAddr, ver, True)
    version = i2c.read(i2cAddr, 1)
    
    sleep(1000)                  # Delay: 1000 milliseconds
    display.scroll(version[0])   # The scroll shows the firmware version
    sleep(3000)                  # Delay: 3000 milliseconds
