#!/bin/bash

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root!"
    exit 1
fi

# Function to run commands safely
run_command() {
    if ! "$@"; then
        echo "Error executing: $*" >&2
        exit 1
    fi
}

# Function to isolate a system (block network traffic)
isolate_system() {
    local ip_address="$1"
    echo "Isolating system with IP: $ip_address"

    # Check if nftables is available
    if command -v nft &>/dev/null; then
        run_command nft add rule ip filter input ip saddr "$ip_address" drop
        run_command nft add rule ip filter output ip daddr "$ip_address" drop
    else
        run_command iptables -A INPUT -s "$ip_address" -j DROP
        run_command iptables -A OUTPUT -d "$ip_address" -j DROP
    fi

    echo "System $ip_address has been isolated."
}

# Function to remove isolation
remove_isolation() {
    local ip_address="$1"
    echo "Removing isolation for IP: $ip_address"

    if command -v nft &>/dev/null; then
        run_command nft delete rule ip filter input ip saddr "$ip_address" drop
        run_command nft delete rule ip filter output ip daddr "$ip_address" drop
    else
        run_command iptables -D INPUT -s "$ip_address" -j DROP
        run_command iptables -D OUTPUT -d "$ip_address" -j DROP
    fi

    echo "Isolation removed for $ip_address."
}

# Main script logic
if [[ $# -ne 2 ]]; then
    echo "Usage: sudo ./isolate.sh <isolate/remove> <IP_ADDRESS>"
    exit 1
fi

action="$1"
target_ip="$2"

case "$action" in
    isolate) isolate_system "$target_ip" ;;
    remove) remove_isolation "$target_ip" ;;
    *) echo "Invalid action! Use 'isolate' or 'remove'." && exit 1 ;;
esac
