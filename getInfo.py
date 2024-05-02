import serial
import time
import platform
port = '/dev/ttyUSB0'
baudrate = 115200
ser = serial.Serial()
ser.port = port
ser.baudrate = baudrate
ser.timeout = 1


#ログを読み取るための基礎コード
ser.open()
while True:
    # シリアルポートからデータを読み取ります
    line = ser.readline()
        
    # 読み取ったデータが空でない場合、データを表示します
    if line:
        print(line.decode('utf-8').strip())