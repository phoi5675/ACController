import serial
import const
import time

if __name__ == '__main__':
    arduino = serial.Serial(const.port, 9600)
    time.sleep(1)
    ch = input()
    ch = ch.encode('utf-8')
    
    time.sleep(1)
    arduino.write(ch)
