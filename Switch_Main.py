#!/usr/bin/python3

from netmiko import ConnectHandler
import os
import time
import datetime
import json
import Email  # Assuming you have implemented the Email module

device_list = '/home/USER_NAME/Switch/Switches.json'
backup_filename = 'SW-Config-Backup-' + '{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()) + '.cfg'
# vlan_filename = 'RTR-Show-VLAN-' + '{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()) + '.txt'

success_messages = []
failure_messages = []

with open(device_list) as json_file:
    data = json.load(json_file)
    # Change data['switch_list'] to data['switch_list'] if you are using switch.json
    for switch in data['switch_list']:
        cisco_2960 = {
            'device_type': 'cisco_ios',
            'host': switch['ip'],
            'username': 'USER_NAME',    # Provide SSH username
            'password': 'PASSWORD',    # Provide SSH password
            'secret': 'PASSWORD',     # Optional, defaults to ''
        }

        try:
            net_connect = ConnectHandler(**cisco_0000)
        except Exception as e:
            failure_messages.append(f"Failed to connect to {switch['hostname']}: {str(e)}")
            continue

        try:
            net_connect.enable()

            output_run_config = net_connect.send_command("show running-config")
            # output_vlan = net_connect.send_command("show vlan-switch")

            net_connect.exit_enable_mode()
            net_connect.disconnect()

            # Create a separate directory for each device if not exists.
            backup_dir = '/home/USER_NAME/Switch/' + switch['hostname']
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            # Write the device running-config to a file.
            backup_filepath = os.path.join(backup_dir, backup_filename)
            with open(backup_filepath, 'w') as f0:
                f0.write(output_run_config)

            success_messages.append(f"Successfully backed up {switch['hostname']} configuration.")
        except Exception as e:
            failure_messages.append(f"Failed to backup {switch['hostname']} configuration: {str(e)}")

# Construct the email subject and body for success
success_subject = "IT-Alert: Network Devices Backup Script Execution - Success"
success_body = "Hello Team, \n \nThe automated script successfully completed the configuration backup for the following network devices:\n\n"

# Append the device names to the body for success
for success_message in success_messages:
    success_body += f"{success_message}\n"

success_body += "\nThank you!\n_ _ \nRegards, \nKishor Khande.\n------------------------------------------------------------------------------------------------------\n This is a system-generated alert. We request you not reply to this message. \n------------------------------------------------------------------------------------------------------"

# Send the success email
to_address_success = "YOUR@EMAIL.ID"  # Replace with the actual recipient email address for success
if success_messages:
    Email.send_email(success_subject, success_body, to_address_success)

# Construct the email subject and body for failure
failure_subject = "IT-Alert: Network Devices Backup Script Execution - Failure"
failure_body = "Hello Team, \n \nThe automated script encountered failures while taking the configuration backup of the following network devices:\n\n"

# Append the device names to the body for failure
for failure_message in failure_messages:
    failure_body += f"{failure_message}\n"

failure_body += "\nThank you!\n_ _ \nRegards, \nKishor Khande.\n------------------------------------------------------------------------------------------------------\n This is a system generated alert. We request you not reply to this message. \n------------------------------------------------------------------------------------------------------"

# Send the failure email
to_address_failure = "YOUR@EMAIL.ID"  # Replace with the actual recipient email address for failure
if failure_messages:
    Email.send_email(failure_subject, failure_body, to_address_failure)