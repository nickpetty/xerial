import serial
import time
import thread
import os
class Xerial():

	def __init__(self, port=None, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0, carriage=False, newline=False, log=False):
		self.ser = serial.Serial()
		self.ser.port=port 
		self.ser.baudrate=int(baudrate) 
		self.ser.bytesize=int(bytesize)
		self.ser.parity=str(parity) 
		self.ser.stopbits=float(stopbits) 
		self.ser.timeout=timeout
		self.ser.xonxoff=int(xonxoff)
		self.ser.rtscts=int(rtscts)
		self.carriage = carriage
		self.newline = newline
		if log != False:
			self.log = True
		else:
			self.log = False
		if self.log == True:
			logName = str(self.ser.port.split('/')[len(self.ser.port.split('/'))-1])+'='+str(time.strftime("%m:%d:%Y")) +'-'+ str(time.strftime("%I:%M:%S"))
			self.logFile = open(logName+".txt", 'w')


	def connect(self):
		try:
			self.ser.open()
		except:
			print 'Could not connect to ' + str(port)
			exit()
		if not self.ser.is_open:
			print 'Could not connect to ' + str(port)
			exit()
			

	def terminal(self):
		if self.ser.is_open:
			print 'Connected!'
			print "Use '>q' to exit..."
			print

		inputBuffer = ''

		thread.start_new_thread(self.listen, ())

		while inputBuffer != '>q':
			
			inputBuffer = raw_input()
			if self.log == True:
				self.logFile.write(inputBuffer+'\n')

			if inputBuffer == '>q':
				self.ser.close()
				return
			self.write(inputBuffer)

		ser.close()

		return

	def write(self, inputBuffer):
		self.ser.write(inputBuffer)
		if self.carriage:
			self.ser.write('\r')
		if self.newline:
			self.ser.write('\n')

	def listen(self):
		while True:
			try:
				line = self.ser.readline().strip('\n')
				print line
				if self.log == True:
					logFile.write(line)

			except:
				return

