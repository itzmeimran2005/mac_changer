#!/usr/bin/env python3

import subprocess
import optparse
import re
import random

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network Interface (e.g., eth0)")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address (e.g., 00:11:22:33:44:55)")
    parser.add_option("-r", "--random", action="store_true", dest="random_mac", help="Generate a random MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    return options

def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface], encoding='utf-8')
        mac_address_search = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
        if mac_address_search:
            return mac_address_search.group(0)
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def generate_random_mac():
    mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Main program
options = get_arguments()

current_mac = get_current_mac(options.interface)
if current_mac:
    print(f"[i] Current MAC: {current_mac}")
else:
    print("[-] Could not read MAC address.")

if options.random_mac:
    new_mac = generate_random_mac()
    print(f"[+] Generated Random MAC: {new_mac}")
elif options.new_mac:
    new_mac = options.new_mac
else:
    print("[-] No MAC specified. Use --mac or --random.")
    exit()

change_mac(options.interface, new_mac)

updated_mac = get_current_mac(options.interface)
if updated_mac == new_mac:
    print(f"[✓] MAC address changed successfully to {updated_mac}")
else:
    print("[-] MAC address change failed.")
