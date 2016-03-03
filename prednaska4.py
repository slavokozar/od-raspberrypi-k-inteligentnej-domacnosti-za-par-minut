import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us 
import socket
import sys
from Classes.ADC import *
from Classes.SIPO import *


GPIO.setmode(GPIO.BOARD)

adc = ADC(33,31,35)

HOST, PORT = '127.0.0.1', 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT

while True:
	try:
		
		client_connection, client_address = listen_socket.accept()
		request = client_connection.recv(1024)

		method, url, protocol = request.split('\r\n', 1)[0].split(' ')
	    
		print(method + ' ' + url)
	    
		http_response = protocol;
		if(method == 'GET'):
			if(url == '/adc'):
				http_response += ' 200 OK'
				http_response += '\n\n'
				http_response += str(adc.read())
			else:
				http_response += ' 404 Not Found'	

		else:
			http_response += ' 501 Not Implemented'

		print http_response
		print ('\n');
		client_connection.sendall(http_response)
		client_connection.close()    

	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()




