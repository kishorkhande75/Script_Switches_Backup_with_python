# Network Device Configuration Backup Script

## Overview
This script automates the process of backing up the configuration of network devices. It uses the Netmiko library for SSH connectivity to Cisco devices and sends the show running-config command to retrieve the running configuration. The script is designed to work with a list of network devices specified in a JSON file.

## Files
1. '**Switch_main.py**'
This is the main script file.
It reads the list of network devices from a JSON file (Switch.json).
Connects to each device using SSH and retrieves the running configuration.
Saves the running configuration to a timestamped backup file in a designated directory.
Sends success and failure email notifications using the Email module.

2. '**Switch.json**'
<ul> JSON file containing a list of network devices.
<ul> Each device has a hostname and IP address.

3. '**Email.py**'
<ul> Module for sending email notifications.
<ul> Uses the '**smtplib'** library to connect to an SMTP server and send emails.
<ul> The email subject and body are provided by the main script.

## Usage
1. Modify the '**Switch.json**' file to include the hostnames and IP addresses of the network devices you want to backup.

2. Replace placeholder values in the '**Switch_main.py**' script:

Replace '**USER_NAME**', '**PASSWORD**', and '**EMAIL_PASSWORD**' with your actual credentials.
Set the correct email addresses for to_address_success and to_address_failure.

3. Ensure that the required Python packages are installed. You can install them using:

**Copy code**
<code> pip install netmiko</code>

4. Run the script:

**Copy code**
<code>python Switch_main.py</code>

# Email Configuration
The script uses a Gmail account to send email notifications. If you're using a different email provider, modify the SMTP server settings in the '**Email.py**' file.
Notes
The script creates a separate directory for each network device inside the specified directory ('**/home/USER_NAME/Switch/**'). Ensure that the script has write permissions to this directory.

Review email security considerations, such as enabling "less secure apps" for Gmail or using an App Password.

**Note:** This README provides a general overview and instructions. Ensure you thoroughly understand the script and make necessary adjustments based on your specific requirements and security considerations.