# GhostNetwork Tool

# The GhostNetwork Tool is a powerful cyber warfare utility designed for advanced network operations such as reconnaissance, microsegmentation, and DNS spoofing. This tool allows users to execute stealthy operations, manipulate network traffic, and gain significant advantages in digital confrontations.

# Features

- Microsegmentation Configuration: Secure your network by implementing firewall rules and launching a captive portal to enhance operational stealth.

- Network Scanning: Efficiently identify active hosts and services within your local network environment using `nmap` for Linux and PowerShell for Windows.

- DNS Spoofing: Skillfully manipulate DNS responses to mislead adversaries and confuse their navigation.

- Captive Portal: Create an enticing web page that targets unsuspecting users, drawing them into your network trap.

- Cross-Platform Compatibility: Operates seamlessly on both Linux and Windows systems, ensuring versatility and adaptability.

# Installation Prerequisites

- Ensure Python 3.x is installed on your system.
- Install `pip`, the package installer for Python, if not already available.
- For Linux users, ensure you have `iptables` and `dnsmasq` installed.
- For Windows users, PowerShell must be available for executing commands.# Steps to Install

1. Clone the repository to your local machine:
   git clone https://github.com/Script-Sculptor/GhostNetwork
   && cd GhostNetwork

2. Install the required Python packages:

pip install -r requirements.txt


3. Install Nmap (Linux):

On Debian/Ubuntu:

sudo apt-get install nmap

On Red Hat/CentOS:

sudo yum install nmap


4. Install dnsmasq (Linux):

On Debian/Ubuntu:

sudo apt-get install dnsmasq


5. Run the GhostNetwork Tool:

python ghost_network_tool.py



Usage

Once the tool is running, follow the on-screen instructions to execute various operations. The main menu provides the following options:

1. Configure Microsegmentation: Sets up firewall rules and starts the captive portal. This helps in managing network traffic effectively and ensuring stealth during operations.


2. Control Microsegmentation: Allows dynamic management and adjustments of the microsegmentation settings based on real-time observations.


3. Scan Network: Conduct a reconnaissance operation to identify active hosts and services in your network. The tool uses nmap for Linux and PowerShell for Windows to perform these scans.


4. Perform DNS Spoofing: Initiates a DNS spoofing attack, utilizing dnsmasq on Linux to manipulate DNS responses. This feature is also implemented for Windows environments using PowerShell.


5. Help: Displays a comprehensive help menu, detailing the functionalities of each available option and providing tactical insights.


6. Exit: Cleanly exits the tool, ensuring that all operations are terminated properly.



Important Notes

Ensure that you have administrative or root access to apply firewall rules and run network scanning operations.

Use the tool responsibly and within legal boundaries. Unauthorized access to networks and devices is illegal and unethical.

Regularly check for updates to the tool, as new features and enhancements are continuously being developed.
