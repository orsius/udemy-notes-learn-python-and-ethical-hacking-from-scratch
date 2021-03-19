#!/usr/bin/env python3

# python3 mac_change.py -i eth0 -m 00: 11: 22: 33: 44: 55

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def print_interface_nfo(interface):
    print("[+] printing ifconfig for interface: " + interface)
    subprocess.call("ifconfig " + interface, shell=True)


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
print_interface_nfo(options.interface)
