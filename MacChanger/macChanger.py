#!/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New MAC Address")
    (options_val, arguments) = parser.parse_args()
    if not options_val.interface:
        parser.error("[-] Please specify an interface use --help for more info")
    elif not options_val.new_mac:
        parser.error("[-] Please specify a mac address use --help for more info")
    return options_val


def change_mac(interface_val, new_mac_val):
    print("[+] The MAC address will be changes for'\t'" + interface_val + "'\t'to'\t'" + new_mac_val)

    subprocess.call(["ifconfig " + interface_val + " down "], shell=True)
    subprocess.call(["ifconfig " + interface_val], shell=True)
    subprocess.call(["ifconfig " + interface_val + " hw ether " + new_mac_val], shell=True)
    subprocess.call(["ifconfig " + interface_val + " up "], shell=True)


def get_current_mac_address(interface_val):
    ifconfig_result = subprocess.check_output(["ifconfig " + interface_val], shell=True)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No MAC address for the given interface")
    subprocess.call(["exit"], shell=True)


options = get_arguments()
current_mac = get_current_mac_address(options.interface)
print("The current MAC Address is:" + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac_address(options.interface)

if current_mac == options.new_mac:
    print("[+] The New MAC Address is:" + str(current_mac))
else:
    print("[-] The MAC Address did not change")

