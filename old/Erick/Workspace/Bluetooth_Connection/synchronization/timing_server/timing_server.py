import bluetooth
import time
import RPi.GPIO as GPIO
SLEEP_TIME = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

while 1:	#Wait for a connection
	print('waiting for a connection')
	connection, client_address = server_sock.accept()
	GPIO.output(18,GPIO.HIGH)
	try:
		print('connection made')
		# Receive the data         
		data = (connection.recv(1024))
		print(data)
		current = time.time()
		
		parsed = data.split(',')
		id = parsed[0]
		diff = float(parsed[2])
		expected_time = float(parsed[1])

		# device is the latency initializer
		if (id == 'i'):
			latency = abs(current - diff)
		# reads initializers latency
		else:
			latency = float(parsed[3])

#		print (latency)
		final = time.time() - latency

		packet = str(latency)
		connection.sendall(packet)
		while(final < expected_time):
			final = time.time() - latency
		print('out')

		while True:
#			print('ON')
			GPIO.output(18, GPIO.HIGH)
			time.sleep(SLEEP_TIME)
#			print('OFF')
			GPIO.output(18, GPIO.LOW)
			time.sleep(SLEEP_TIME)

	finally:
		# Clean up the connection
		#        print("Closing current connection")
		connection.close()

	# instantiate reconnection
	#server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

	#port = 1
	#server_sock.bind(("",port))
	#server_sock.listen(1)  


