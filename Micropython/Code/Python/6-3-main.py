# Imports go at the top
from microbit import *

# Car I2C address 
i2cAddr = 0x29

# For Pins
s1  = 16       #S1 Pin
s2  = 17       #S2 Pin
s3  = 18       #S3 Pin
s4  = 19       #S4 Pin
i2cBuf = bytearray([0x00, 0x00])

# S1--S4 pins mode
s1ToS4 = 15
pwmMode = 1
servoMode = 2

# Control S1--S4 pins output PWM signal function
# pin: s1 -- s4
# pwm: 0 -- 200
def setPinPwm(pin, pwm):
    if pin == s1:          
        i2cBuf[0] = s1 
    elif pin == s2:
        i2cBuf[0] = s2
    elif pin == s3:
        i2cBuf[0] = s3
    elif pin == s4:
        i2cBuf[0] = s4
    else:
        return
    i2cBuf[1] = pwm
    i2c.write(i2cAddr, i2cBuf)

# Set the S1--S4 pin mode
# mode: 1 = PWM mode, 2 = servo mode
def setPinMode(mode):
    if mode == servoMode:          
        i2cBuf[1] = servoMode 
    elif mode == pwmMode:
        i2cBuf[1] = pwmMode
    else:
        return
    i2cBuf[0] = s1ToS4
    i2c.write(i2cAddr, i2cBuf)

# Set the pins S1--S4 to PWM mode
setPinMode(pwmMode)

# Code in a 'while True:' loop repeats forever
while True:
    for pwm in range(200):
        setPinPwm(s1, pwm)    
        setPinPwm(s2, pwm)    
        setPinPwm(s3, pwm)    
        setPinPwm(s4, pwm)    
        sleep(10)

    
