#!/usr/bin/python3

from netmiko import ConnectHandler
import os
import time
import datetime
import json
import Email

device_list = 'C:\\Users\\ab\\Documents\\Switch\\Switches.json'
backup_filename = 'SW-Config-Backup-' + '{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()) + '.cfg'
# vlan_filename = 'RTR-Show-VLAN-' + '{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()) + '.txt'

with open(device_list) as json_file:
    data = json.load(json_file)
    # Change data['switch_list'] to data['switch_list'] if you are using switch.json
    for switch in data['switch_list']:
        cisco_2960 = {
    	    'device_type': 'cisco_ios',
    	    'host':   switch['ip'],
    	    'username': 'abc',    # Provide SSH username
    	    'password': 'XYZ',    # Provide SSH password
    	    'secret': 'XYZ',     # Optional, defaults to ''
	}

        try:
            net_connect = ConnectHandler(**cisco_2960)
        except:
            continue

        net_connect.enable()

        output_run_config = net_connect.send_command("show running-config")
        # output_vlan = net_connect.send_command("show vlan-switch")

        net_connect.exit_enable_mode()
        net_connect.disconnect()

        #Create a separate directory for each device if not exists.
        backup_dir = 'C:\\Users\\ab\Documents\\Backup\\'+switch['hostname']
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        #Write the device running-config to a file.
        f0 = open(backup_dir+'\\'+backup_filename, 'w')
        f0.write(output_run_config)
        f0.close()
    Email.Email()
    