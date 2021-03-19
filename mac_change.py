#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",
                  help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

# interface = input("interface > (e.g. wlan0)")
# new_mac = input("new_mac > (e.g. 00:11:22:33:44:77 )")
interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


print("[+] printing ifconfig " + interface)
subprocess.call("ifconfig " + interface, shell=True)


# python3 mac_change.py - i eth0 - m 00: 11: 22: 33: 44: 55
