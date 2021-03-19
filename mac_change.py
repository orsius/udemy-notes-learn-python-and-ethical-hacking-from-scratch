#!/usr/bin/env python3

# python3 mac_change.py -i eth0 -m 00: 11: 22: 33: 44: 55

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error(
            "[-] Please specify a mac address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def print_interface_nfo(interface):
    print("[+] printing ifconfig for interface: " + interface)
    subprocess.call("ifconfig " + interface, shell=True)


options = get_arguments()
change_mac(options.interface, options.new_mac)
print_interface_nfo(options.interface)
