from flask import Flask, request, render_template
import serial
import time
import platform


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.json
    x = data.get('x_axis')
    y = data.get('y_axis')
    
    setValue(x,y)
    
    
    return 'OK'


#postによって受け取った値で入力値を更新
def setValue(x,y):
    input_x=convertRange(int(x))
    input_y=convertRange(int(y))
    
    ser.write(bytes([250, input_y, input_x, 0]))
    
    
#input range -100~100 --> output range 127~0
def convertRange(x):
    if x >=1:
        #x=1~100 out=127~65
        return int(63*x/100)+64
    if x <= -1:
        #x=-1~-100 out=1~63
        return int(63*abs(x)/100)
    
    return 0


if __name__ == '__main__':
    input_x=0
    input_y=0
    #初期設定
    port = '/dev/ttyUSB0'## 必要に応じて変更
    baudrate = 115200
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.timeout = 1
    # if platform.system() == 'Windows':
    #     ser.setDTR(False)
    #     ser.setRTS(False)
    ser.open()
    # serial mode
    ser.write(bytes([251, 2, 0, 0]))#251 モード変更命令，2 シリアル信号
    time.sleep(1)
    
    
    app.run(host='0.0.0.0')
    

    