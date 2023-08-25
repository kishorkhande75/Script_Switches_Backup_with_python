## Requirement to run python script:-
**Python installed on machine**


## What in python script:-
1. Date and time
2. Email Configuration
3. Json file for multiple host


## Network Devices Configuration Backup and Email Alert Script

This guide outlines the setup and usage of a Python script that automates the process of backing up the configuration of network devices and sending an email alert upon successful execution. The script utilizes the Netmiko library for SSH connections to network devices and the smtplib library for sending emails.

## Files Included

1. **email.py:** This file contains the code for sending email alerts using the smtplib library.
2. **Switches.json:** A JSON configuration file containing a list of network devices to be backed up.
3. **Switches.py:** The main Python script responsible for connecting to network devices, retrieving configuration, and sending alerts.

## Prerequisites

1. Install the required Python libraries:
    <code>pip install netmiko</code>

2. Update the necessary information in the script files:

1. In **Switches.json**, replace the IP addresses and hostnames of your network devices.
2. In **Switches.py**, update the following fields within the cisco_2960 dictionary for each device:

    **I.** username: Your SSH username

    **II.** password: Your SSH password

    **III.** secret: Optional, the enable mode password (if applicable)

## How to Use
1. Place the three script files (**email.py**, **Switches.json**, and **Switches.py**) in the same directory.

2. Open a command prompt or terminal and navigate to the directory containing the script files.

3. Run the **Switches.py** script:

    **I. python Switches.py**
    The script will connect to each network device, retrieve the running configuration, and save it to a separate directory named after the device's hostname.

4. Upon completion of the backup process, an email alert will be sent using the **email.py** script. Make sure to provide the appropriate email addresses and passwords in the script.

## Note

<h3>&#x2022;</h3>Ensure that the necessary security measures are taken to protect sensitive information such as passwords and email credentials.

\*The script assumes you are using Cisco devices with the `**cisco_ios**` device type. Modify the script accordingly if you are working with  different device types.

## Disclaimer
This script is provided as-is and should be thoroughly tested in a controlled environment before being used in a production setting. Make sure to understand the potential risks associated with automating network device configurations and ensure proper backups are maintained.