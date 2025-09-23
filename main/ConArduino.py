import serial
import time
import sys

py_serial = serial.Serial(
    # serial port 설정
    port = "com5",
    # 보드 레이트 (통신 속도)
    baudrate= 9600)

py_serial.write('1'.encode())
time.sleep(sys.argv)
py_serial.write('2'.encode())
time.sleep(sys.argv)

print('창문')