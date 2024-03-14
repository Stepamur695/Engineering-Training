import RPi.GPIO as GPIO
#import funcs

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def decimalToBinary(value):
    if value < 0: #Base case if number is a negative
        return 'Not positive'
    elif value == 0: #Base case if number is zero
        return str(0)
    else:
        number = [0 for i in range(8)]
        bin_num = bin(value)
        i = -1
        while bin_num[i] != 'b':
            number[i] = int(bin_num[i])
            i -= 1
        return number




try:
    while True:
        num = input("Type a number from 0 to 255: ")
        #print(type(num))
        try:
            num = int(num)
            #print(type(num))
            #print(num)
            #print (0 <= num <= 255)
            if 0 <= num <= 255:
                #print (0 <= num <= 255)
                GPIO.output(dac, decimalToBinary(num))
                #print (0 <= num <= 255)
                voltage = float(num) / 255.0 * 3.3
                print(f"Output voltage is about {voltage:.4} volt")
            else:
                if num < 0:
                    print("Number have to be >=0! Try again...")
                elif num > 255:
                    print("Number is out of range [0,255]! Try again...")  
        except Exception:
            if num == "q": break
            print("You have to type a number, not string! Try again...")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")



    