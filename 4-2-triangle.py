import RPi.GPIO as GPIO
from time import sleep
#from funcs import dec2bin
#from matplotlib import pyplot as plt
#import numpy as np

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
t = 0 
x = 0

def decimalToBinary(value):
    if value < 0: #Base case if number is a negative
        return 'Not positive'
    elif value == 0: #Base case if number is zero
        number = [0 for i in range(8)]
        return number
    else:
        number = [0 for i in range(8)]
        bin_num = bin(value)
        i = -1
        while bin_num[i] != 'b':
            number[i] = int(bin_num[i])
            i -= 1
        return number


try:
    period = float(input("Type a period for signal: "))
    

    while True:
        GPIO.output(dac, decimalToBinary(x))
        

        if   x == 0:    inc_flag = 1
        elif x == 255:  inc_flag = 0

        x = x + 1 if inc_flag == 1 else x - 1

        sleep(period/512)
        t += 1
        

except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
    