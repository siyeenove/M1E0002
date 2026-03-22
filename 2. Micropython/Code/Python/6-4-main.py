# Imports go at the top
from microbit import *

# Car I2C address 
i2cAddr = 0x29

# Type of battery
aaBattery3 = bytearray([0x01])        # 3 AA batteries
aaBattery4 = bytearray([0x02])        # 4 AA batteries
aaBattery5 = bytearray([0x03])        # 5 AA batteries
aaBattery6 = bytearray([0x04])        # 6 AA batteries
lithiumBattery1 = bytearray([0x05])   # 1 lithium battery
lithiumBattery2 = bytearray([0x06])   # 2 lithium batteries

# Initialize the I2C communication interface
i2c.init()


# Code in a 'while True:' loop repeats forever
while True:
    # Read the level of 3 AA batteries
    i2c.write(i2cAddr, aaBattery3, True)
    batLevel = i2c.read(i2cAddr, 1)
    
    sleep(1000)                  # Delay: 1000 milliseconds
    display.scroll(batLevel[0])  # Scroll display of battery level
    sleep(3000)                  # Delay: 3000 milliseconds
