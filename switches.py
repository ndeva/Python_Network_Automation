#!/usr/bin/env python3
import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

# loop through the switches using ip addresses
for n in range(71, 76):
    HOST = "192.168.122.{}".format(n).encode()
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")

    # loop for creating 20 vlans in each switch from vlan 2 to vlan 20
    for v in range(2, 21):
        tn.write("vlan {}\n".format(v).encode())
        tn.write("name VLAN_{}\n".format(v).encode())

    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
