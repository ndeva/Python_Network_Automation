#!/usr/bin/env python3

from devices_inventory.switches_invt import *

from netmiko import ConnectHandler

# opens the switched_campus_configs file each line contains configurations for access switches
with open('switched_campus_configs') as f:
    lines = f.read().splitlines()
print(lines)

# access switches
all_devices = [access_S5, access_S4, access_S3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

# open configuration file for core switches
with open('core_switches_configs') as f:
    lines = f.read().splitlines()
print(lines)

# core switches
all_devices = [core_S2, core_S1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
