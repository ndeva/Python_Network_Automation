#!/usr/bin/env python3

from devices_inventory.switches_invt import access_S5, access_S4, access_S3, core_S2, core_S1
from netmiko import ConnectHandler

# initial configuration of access switches
with open('access_switches_configs') as f:
    lines = f.read().splitlines()
print(lines)


all_devices = [access_S5, access_S4, access_S3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

# initial configuration of core switches

with open('core_switches_configs') as f:
    lines = f.read().splitlines()
print(lines)


all_devices = [core_S2, core_S1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
