#!/usr/bin/env python
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
       parser.error("[-] Please specify an interface use --help for more info")
    elif not  options.new_mac:
        parser.error("[-] Please specify a mac address use --help for more info")
    return options


def change_mac(interface_val, new_mac_val):
    print("[+] The MAC address will be changes for'\t'" + interface_val + "'\t'to'\t'" + new_mac_val)

    subprocess.call(["ifconfig " + interface_val + " down "], shell=True)
    subprocess.call(["ifconfig " + interface_val], shell=True)
    subprocess.call(["ifconfig " + interface_val + " hw ether " + new_mac_val], shell=True)
    subprocess.call(["ifconfig " + interface_val + "up "], shell=True)
    subprocess.call(["ifconfig " + interface_val], shell=True)
    subprocess.call(["exit"], shell=True)


options = get_arguments()
change_mac(options.interface, options.new_mac)

# "02:42:0f:10:67:28"
# 02:42:46:14:2f:a2
