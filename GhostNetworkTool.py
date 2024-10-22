import os
import platform
import subprocess
import nmap
import logging
from colorama import Fore, Style

# Configure logging
logging.basicConfig(filename='ghost_network.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GhostNetworkTool:
    def __init__(self):
        self.scanner = nmap.PortScanner()
    
    def display_banner(self):
        print(Fore.CYAN + "Welcome to GhostNetwork Tool")
        print(Fore.YELLOW + "A powerful utility for cyber warfare operations.")
        print(Style.RESET_ALL)

    def configure_microsegmentation(self):
        print(Fore.YELLOW + "Configuring microsegmentation...")
        os.system("iptables -A INPUT -s 192.168.1.0/24 -j DROP")
        logging.info("Microsegmentation configured to block inbound traffic from subnet 192.168.1.0/24.")
        print(Fore.GREEN + "Microsegmentation configured successfully.")
    
    def scan_network(self):
        print(Fore.YELLOW + "Scanning the network...")
        try:
            self.scanner.scan(hosts='192.168.1.0/24', arguments='-sP')
            for host in self.scanner.all_hosts():
                print(f"Host: {host} ({self.scanner[host].hostname()})")
                print(f"State: {self.scanner[host].state()}")
            logging.info("Network scan completed successfully.")
        except Exception as e:
            logging.error(f"Network scanning failed: {e}")
            print(Fore.RED + f"Error during network scan: {e}")

    def perform_dns_spoofing(self):
        """Launch a DNS spoofing attack to manipulate the network's informational landscape."""
        print(Fore.YELLOW + "Initiating the DNS spoofing operation...")
        system = platform.system()
        if system == 'Linux':
            try:
                subprocess.run(["dnsmasq"], check=True)
                print(Fore.GREEN + "DNS spoofing operation initiated using dnsmasq on Linux.")
                logging.info("DNS spoofing initiated on Linux.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error initiating dnsmasq: {e}")
                print(Fore.RED + f"Error initiating dnsmasq: {e}")
        elif system == 'Windows':
            try:
                dns_spoof_command = "Start-Process -FilePath 'dnsspoof.exe' -ArgumentList '-i', 'eth0', '-d', 'example.com', '192.168.1.2'"
                subprocess.run(["powershell", "-Command", dns_spoof_command], check=True)
                print(Fore.GREEN + "DNS spoofing operation initiated using a Windows-compatible tool.")
                logging.info("DNS spoofing initiated on Windows.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error initiating DNS spoofing on Windows: {e}")
                print(Fore.RED + f"Error initiating DNS spoofing: {e}")

    def start_captive_portal(self):
        """Start a captive portal to lure unsuspecting users."""
        print(Fore.YELLOW + "Starting the captive portal...")
        # Assuming a simple Python-based HTTP server for demonstration
        try:
            os.system("python3 -m http.server 8080")
            print(Fore.GREEN + "Captive portal is running on port 8080.")
            logging.info("Captive portal started on port 8080.")
        except Exception as e:
            logging.error(f"Error starting captive portal: {e}")
            print(Fore.RED + f"Error starting captive portal: {e}")

    def show_help(self):
        """Display a help menu with tool functionalities."""
        print(Fore.YELLOW + "Help Menu:")
        print("1. Configure Microsegmentation: Set up firewall rules.")
        print("2. Scan Network: Identify active hosts and services.")
        print("3. Perform DNS Spoofing: Manipulate DNS responses.")
        print("4. Start Captive Portal: Launch a web page to lure users.")
        print("5. Exit: Close the tool.")
        print(Style.RESET_ALL)

    def main_menu(self):
        """Main menu loop for user interaction."""
        while True:
            self.display_banner()
            print(Fore.CYAN + "Main Menu:")
            print("1. Configure Microsegmentation")
            print("2. Scan Network")
            print("3. Perform DNS Spoofing")
            print("4. Start Captive Portal")
            print("5. Help")
            print("6. Exit")
            print(Style.RESET_ALL)

            choice = input("Select an option: ")
            if choice == '1':
                self.configure_microsegmentation()
            elif choice == '2':
                self.scan_network()
            elif choice == '3':
                self.perform_dns_spoofing()
            elif choice == '4':
                self.start_captive_portal()
            elif choice == '5':
                self.show_help()
            elif choice == '6':
                print(Fore.GREEN + "Exiting the tool...")
                logging.info("Tool exited by user.")
                break
            else:
                print(Fore.RED + "Invalid selection. Please try again.")

if __name__ == "__main__":
    tool = GhostNetworkTool()
    tool.main_menu()
