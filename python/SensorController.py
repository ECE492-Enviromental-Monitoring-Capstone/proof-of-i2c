import time
from datetime import datetime
import board
import adafruit_ahtx0
import sys
import os
import pyaudio 

"""def initialize_microphone():
	pyaudioInstance = pyaudio.PyAudio()
	for i in range(pyaudioInstance.get_device_count()):
		print(pyaudioInstance.get_device_info_by_index(i).get('name'))"""

	
def initialize_temhum_sensor():
	# Create sensor object, communicating over the board's default I2C bus
	global sensor
	i2c = board.I2C()  # uses board.SCL and board.SDA
	sensor = adafruit_ahtx0.AHTx0(i2c)

def print_temhum_result():
		print("\nTemperature: %0.1f C" % sensor.temperature)
		print("Humidity: %0.1f %%" % sensor.relative_humidity)

def record_temhum_result(period):
	if sensor is not None:
		file = open("tem&hum_data.txt","a")
		print("Start recording")
		for p in range(period):
			file.write("Temp={0:0.1f}*C Humidity={1:0.1f}  ".format(sensor.temperature,sensor.temperature))
			file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
			time.sleep(1)
		print("recording is done")
	else:
		file = open("log.txt","a")
		file.write("NAN ")
		file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
	#file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
	file.close


def main():
	#initialize all sensors
	initialize_temhum_sensor()	
	command = ""
	
	while True:
		command = str(input())
		#print("user input ="+command)
		#print(command == "printresult")
		
		if command == "printresult":
			print_temhum_result()
			time.sleep(2)
		
		elif command == "recordresult":
			record_temhum_result(10)
			time.sleep(2)
		
		elif command == "exit":
			sys.exit()

if __name__ == "__main__":
	main()

