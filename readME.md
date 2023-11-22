# Network Device Configuration Backup Script

## Overview
This script automates the process of backing up the configuration of network devices. It uses the Netmiko library for SSH connectivity to Cisco devices and sends the '**show running-config**' command to retrieve the running configuration. The script is designed to work with a list of network devices specified in a JSON file.

## Files
1. '**Switch_main.py**'
<ul>
<li> This is the main script file.</li>
<li> It reads the list of network devices from a JSON file (Switch.json).</li>
<li> Connects to each device using SSH and retrieves the running configuration.</li>
<li> Saves the running configuration to a timestamped backup file in a designated directory.</li>
<li> Sends success and failure email notifications using the Email module.</li>
</ul>

2. '**Switch.json**'
<ul> 
<li> JSON file containing a list of network devices.</li>
<li> Each device has a hostname and IP address.</li>
</ul>
 
3. '**Email.py**'<ul>
<li> Module for sending email notifications.</li>
<li> Uses the '**smtplib'** library to connect to an SMTP server and send emails.</li>
<li> The email subject and body are provided by the main script.</li>
</ul>

## Usage
1. Modify the '**Switch.json**' file to include the hostnames and IP addresses of the network devices you want to backup.

2. Replace placeholder values in the '**Switch_main.py**' script:
<ul>
<li> Replace '**USER_NAME**', '**PASSWORD**', and '**EMAIL_PASSWORD**' with your actual credentials.</li>
<li> Set the correct email addresses for to_address_success and to_address_failure.</li>
</ul>

3. Ensure that the required Python packages are installed. You can install them using:

**Copy code**
<code> pip install netmiko</code>

4. Run the script:

**Copy code**
<code>python Switch_main.py</code>

# Email Configuration
<ul>
<li>The script uses a Gmail account to send email notifications. If you're using a different email provider, modify the SMTP server settings in the '**Email.py**' file.</li>
</ul>
# Notes
<ul>
<li> The script creates a separate directory for each network device inside the specified directory ('**/home/USER_NAME/Switch/**'). Ensure that the script has write permissions to this directory.
<li> Review email security considerations, such as enabling "less secure apps" for Gmail or using an App Password.</li>
</ul>

**Note:** This README provides a general overview and instructions. Ensure you thoroughly understand the script and make necessary adjustments based on your specific requirements and security considerations.