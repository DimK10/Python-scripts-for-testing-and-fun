#!/usr/bin/env python

import os
import sys
import subprocess
import random as rn
import optparse

#Check root priviledges
if os.getuid() != 0:
	sys.exit("Need to run as root")

#Pass arguments in script
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
parser.add_option("-r", "--random", action="store_true", dest="verbose", help="Random MAC address")
(options, arguments) = parser.parse_args()

interface = options.interface
mac = options.mac

#Make random mac--needs update throws error because not every hex can be assigned in fisrt numbers of mac
if options.verbose == True:
	randMac =''
	for i in range(6):
		rand = rn.randint(0,255)
		if i == 5:
	 		randMac += ("0" + hex(rand).split('x')[-1] if 0<=rand<=15 else hex(rand).split('x')[-1])
		else:	
			randMac += ("0" + hex(rand).split('x')[-1] if 0<=rand<=15 else hex(rand).split('x')[-1]) +':'
#Also can be used the following for hex conversion
# randMac += '{:02x}'.format(rand) makes the number to two hex digits
# delete if i == 5 and on the overall randMac
#randMac = ':'.join(randMac)and the double hex digits generated have : between them


	print("[+] Changing mac address to random of ", interface, " interface")
	subprocess.call(["ifconfig",interface, "down"])
	run = subprocess.call(["ifconfig", interface, "hw", "ether", randMac])
	subprocess.call(["ifconfig", interface, "up"])
	if run == 0:
		print("[+] mac address of " + interface + " changed to " + randMac + " random mac")
	else:
		print("MAC was not changed-random MAC could not be assigned. Try again")
else:
	print("[+] Changing mac address to ", mac, " of ", interface, " interface")
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])
	print("[+] mac address of " + interface + " changed to " + mac + " mac")