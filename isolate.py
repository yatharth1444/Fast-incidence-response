#!/usr/bin/python3

import subprocess
import logging
import os
import sys

def check_root():
    """ Ensure the script is run as root. """
    if os.geteuid() != 0:
        print("This script must be run as root!")
        sys.exit(1)

def run_command(command):
    """ Run a shell command and handle errors. """
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {' '.join(command)}\n{e}")

def isolate_system(ip_address):
    """ Blocks incoming & outgoing traffic for a given IP. """
    logging.info(f"Isolating system with IP: {ip_address}")

    # Check if nftables is available
    nft_available = subprocess.run(["command", "-v", "nft"], capture_output=True).returncode == 0

    if nft_available:
        run_command(["nft", "add", "rule", "ip", "filter", "input", "ip", "saddr", ip_address, "drop"])
        run_command(["nft", "add", "rule", "ip", "filter", "output", "ip", "daddr", ip_address, "drop"])
    else:
        run_command(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"])
        run_command(["iptables", "-A", "OUTPUT", "-d", ip_address, "-j", "DROP"])

    logging.info(f"System {ip_address} has been isolated.")

def remove_isolation(ip_address):
    """ Removes isolation for a given IP. """
    logging.info(f"Removing isolation for IP: {ip_address}")

    nft_available = subprocess.run(["command", "-v", "nft"], capture_output=True).returncode == 0

    if nft_available:
        run_command(["nft", "delete", "rule", "ip", "filter", "input", "ip", "saddr", ip_address, "drop"])
        run_command(["nft", "delete", "rule", "ip", "filter", "output", "ip", "daddr", ip_address, "drop"])
    else:
        run_command(["iptables", "-D", "INPUT", "-s", ip_address, "-j", "DROP"])
        run_command(["iptables", "-D", "OUTPUT", "-d", ip_address, "-j", "DROP"])

    logging.info(f"Isolation removed for {ip_address}")

if __name__ == "__main__":
    check_root()

    logging.basicConfig(filename='incident_response.log', level=logging.INFO)

    if len(sys.argv) != 3:
        print("Usage: sudo python3 isolate.py <isolate/remove> <IP_ADDRESS>")
        sys.exit(1)

    action, target_ip = sys.argv[1], sys.argv[2]

    if action == "isolate":
        isolate_system(target_ip)
    elif action == "remove":
        remove_isolation(target_ip)
    else:
        print("Invalid action! Use 'isolate' or 'remove'.")
        sys.exit(1)
