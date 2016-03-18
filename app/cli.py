#!/usr/bin/python 
import sys
import pkg_resources
pkg_resources.require("pyserial==3.0.1")
import glob
import json
import os
from xerial import Xerial
path = os.path.dirname(os.path.realpath(__file__))

def flags(flag):
	if flag in sys.argv:
		try:
			return sys.argv[sys.argv.index(flag)+1]
		except:
			return False

def showHelp():
	print open(path+'/docs/README.md','r').read()
	print '  Logs can be found in ' + path + "/logs/"		
	print
	print 'Available Ports:'
	print '----------------'		

	for each in glob.glob('/dev/tty.*'):
		print "  > " + str(each)

if __name__ == "app.xerial" or "__main__":
	if len(sys.argv) == 1:
		showHelp()
		exit()

	if '-h' in sys.argv:
		showHelp()
		exit()

	if '-ls' in sys.argv:
		ports = glob.glob('/dev/tty.*')
		if len(ports) > 0:
			for port in ports:
				print port
			exit()
		else:
			print 'No ports found...'
			exit()

	if '-lp' in sys.argv:
		if len(sys.argv) > 2:
			try:
				if not os.path.isdir(path+"/presets"):
					os.makedirs(path+"/presets")
				pf = json.load(open(path+"/presets/"+sys.argv[sys.argv.index('-lp')+1]+".xer"))
			except:
				print 'Could not load ' + sys.argv[sys.argv.index('-lp')+1]
				exit()

			
			print 'Parameters:'
			print '-----------'
			for key in pf:
				print str(key) + ':' + str(pf[key])
			print ''
			exit()

		presets = glob.glob(path+'/presets/*.xer')

		if len(presets) > 0:
			print 'Presets:'
			for preset in presets:
				print '  > '+ str(preset.split('/')[len(preset.split('/'))-1])[:-4]
			exit()
		print 'No presets found.'
		exit()

	if flags("-p") != False:
		#port = sys.argv[sys.argv.index('-c')+1]
		port = flags("-p")

		if '-b' in sys.argv:
			speed = sys.argv[sys.argv.index('-b')+1]
			try:
				speed = int(speed)
			except:
				print '  Please enter a valid baudrate. Usage: -b <baudrate>'
				exit()
		else:
			speed = '9600'

		if '-a' in sys.argv:
			try:
				args = sys.argv[sys.argv.index('-a')+1].split('/')
				if len(args) != 3:
					print '  Invalid arugment format. Usage: -a <int:bytesize>/<str:parity>/<int:stopbits>. Must include all three.'
					exit()

				bytesize = int(args[0])
				if bytesize not in range(4,9):
					print '  Invalid bytesize.  Valid sizes: "5, 6, 7, 8"'
					exit()

				parity = str(args[1])
				validParity = ['N','O','E','M','S']
				if parity not in validParity:
					print '  Invalid parity bit type. Valid types: "N, O, E, M, S"'
					exit()

				validStopbits = [1,1.5,2]
				stopbits = float(args[2])
				if stopbits not in validStopbits:
					print '  Invalid stopbit.  Valid bits: "1, 1.5, 2"'
					exit()

			except:
				print '  Invalid arugment format. Usage: -a <int:bytesize>/<str:parity>/<int:stopbits>. Must include all three.'
				exit()

		else:
			bytesize = 8
			parity = 'N'
			stopbits = 1

		if '-t' in sys.argv:
			try:
				timeout = int(sys.argv[sys.argv.index('-t')+1])
			except:
				print '  Invalid timeout time.  Usage: -t <sec>'
				exit()
		else:
			timeout = None

		if '-hw' in sys.argv:
			handshake = 1
		else:
			handshake = 0

		if '-CR' in sys.argv:
			carriage = True
		else:
			carriage = False

		if '-LF' in sys.argv:
			newline = True
		else:
			newline = False

		if  sys.argv[len(sys.argv)-2] == '-s':
			data = {
			"port":port,
			"speed":speed,
			"bytesize":bytesize,
			"parity":parity,
			"stopbits":stopbits,
			"timeout":timeout,
			"rtscts":handshake,
			"carriage":carriage,
			"newline":newline
			}

			try:
				presetName = sys.argv[sys.argv.index('-s')+1]
				
			except:
				print 'Invalid file name.  Usage: -s <filename>'
				exit()	
			if not os.path.isdir(path+"/presets"):
				os.makedirs(path+"/presets")
			with open(path+"/presets/" + presetName+".xer", 'w') as outfile:
				json.dump(data, outfile)
			exit()

		if '-log' in sys.argv:
			log = True
		else:
			log = False
		
		

	else:
		print '  No port specified.  Usage: "xerial -c <serialport>". Run "xerial" for more options.'
		exit()

	if '-license' == sys.argv[1]:
		print
		print open(path+"/docs/LICENSE.md").read()
		print
		exit()

	if sys.argv[1] == '-l':
		try:
			if not os.path.isdir(path+"/presets"):
				os.makedirs(path+"/presets")
			presetFile = open(path+"/presets/" + sys.argv[2]+".xer", 'r')
			pf = json.load(presetFile)			

		except:
			print "Could not load " + sys.argv[2]+".xer"
			exit()

		print 'Connecting to ' + str(pf["port"]) + ' at speed ' + str(pf["speed"]) + ' - ' + str(pf["bytesize"])+'/'+str(pf["parity"])+'/'+str(pf["stopbits"]) 

		xerial = Xerial(pf["port"], pf["speed"], pf["bytesize"], pf["parity"], pf["stopbits"], pf["timeout"], rtscts=pf["rtscts"], carriage=pf["carriage"], newline=pf["newline"], log=log)
		xerial.connect()
		xerial.terminal()
		exit()

	if '-p' in sys.argv:
		print 'Connecting to ' + sys.argv[sys.argv.index('-p')+1] + ' at speed ' + str(speed) + ' - ' + str(bytesize)+'/'+str(parity)+'/'+str(stopbits) 

		xerial = Xerial(port, speed, bytesize, parity, stopbits, timeout, rtscts=handshake, carriage=carriage, newline=newline, log=log)
		xerial.connect()
		xerial.terminal()
		exit()
	else:
		print "  -p <port> must be included"
		exit()











