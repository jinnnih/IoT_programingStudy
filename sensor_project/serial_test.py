import serial
import time 
import flask import Flask,render_template

app = Flask(__name__)

def read_sensor():
	""" Arduino에서 센서 데이터 1개를 읽어 딕셔너리로 반환"""
	
	try :
		#시리얼 포트 설정 
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #타임아웃은 아두이노에서 데이터가 오지 않았을 때 1초까지 기다리겠다는 뜻
		time.sleep(2)  # 리셋
		line = ser.readline().decode('utf-8').rstrip()
		ser.close()
		humidity, celsius = line.split(',')
		return{
			humidity = float(humidity)
			celsius = float(celsius)
		}
	
	except Exception as e:
		print("센서 오류:", e)
		return {"temperature":None, "humidity":None}

@app.route('/')
def index():
	data = read_sensor()
	return render_template("index.html", sensor=data)

if __name__ == '__main__'
	app.run(debug=True)
	




