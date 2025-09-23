import serial
import time

# class windowCon:
#     def __init__(self, command):
#         self.command = command
#     def __call__(self):
#         py_serial = serial.Serial(
#             # Window
#             port='COM3',   
#             # 보드 레이트 (통신 속도)
#             baudrate=9600
#         )

#         while True:
#             py_serial.write(self.commend.encode())
#             time.sleep(0.1)

class windowCon:
    def __init__(self, command):
        self.command = command
    def __call__(self, command):
        print(self.command)
        py_serial = serial.Serial(
            # Window
            port='COM3',   
            # 보드 레이트 (통신 속도)
            baudrate=9600,
        )

        while True:
            py_serial.write(self.commend.encode())
            time.sleep(0.1)
            print(py_serial.readline())