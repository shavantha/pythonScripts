#!/usr/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="The New MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

#"02:42:0f:10:67:28"
# 02:42:46:14:2f:a2

print("[+] The MAC address will be changes for'\t'" + interface + "'\t'to'\t'" + new_mac)

subprocess.call(["ifconfig " + interface + " down "], shell=True)
subprocess.call(["ifconfig " + interface], shell=True)
subprocess.call(["ifconfig " + interface + " hw ether " + new_mac], shell=True)
subprocess.call(["ifconfig " + interface + "up "], shell=True)
subprocess.call(["ifconfig " + interface], shell=True)
subprocess.call(["exit"], shell=True)




