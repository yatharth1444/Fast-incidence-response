# Incident Response Automation (IRA)

**Author:** Yatharth 
**Email:** [yatharthsingh1444@gmail.com](mailto:yatharthsingh1444@gmail.com)  

---

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Features](#features)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Customization](#customization)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

**Incident Response Automation (IRA)** is a powerful tool designed to help security teams **automate the containment of compromised systems** during an active security incident. By leveraging **firewall rules** (`iptables` or `nftables`), the script isolates affected machines to prevent further spread of a cyber attack.

This script is ideal for:
- **Security professionals** handling active threats.
- **System administrators** managing corporate networks.
- **Cybersecurity researchers** testing response techniques.

---

## How It Works

1. **Identifies the target IP address** of the compromised system.
2. **Blocks all incoming and outgoing traffic** for that IP using either `iptables` or `nftables`.
3. **Logs the action** for auditing and future incident analysis.
4. **Allows removal of isolation** when the threat is mitigated.

---

## Features

✅ Automated system isolation with firewall rules  
✅ Supports both `iptables` and `nftables`  
✅ Logging for auditing and forensic analysis  
✅ Easy to integrate with incident response workflows  
✅ Simple command-line usage  

---

## Requirements

- **Linux-based OS** (Debian, Ubuntu, CentOS, etc.)
- **Python 3.x**
- **Root privileges** to modify firewall rules
- **iptables** or **nftables** installed

---

## Installation & Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yatharth1444/Fast-incidence-response.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd fast_incidence_response
    ```
3. **Ensure execution permissions:**
    ```bash
    chmod +x isolate.py isolate.sh
    ```

---

## Usage

### **Python Version**
To **isolate** a system by its IP address:
```bash
sudo python3 isolate.py isolate <IP_ADDRESS>
```
Example:
```bash
sudo python3 isolate.py isolate 192.168.1.100
```

To **remove isolation**:
```bash
sudo python3 isolate.py remove <IP_ADDRESS>
```
Example:
```bash
sudo python3 isolate.py remove 192.168.1.100
```

### **Bash Version**
To **isolate** a system:
```bash
sudo ./isolate.sh isolate <IP_ADDRESS>
```

To **remove isolation**:
```bash
sudo ./isolate.sh remove <IP_ADDRESS>
```

---

## Customization

- Modify the script to use **UFW** or **firewalld** if your system prefers those over `iptables`.
- Add **email notifications** or **Slack alerts** upon isolation.
- Extend logging capabilities to integrate with **SIEM solutions**.

---

## Security Considerations

 **Use with caution:** Blocking the wrong IP could disrupt services.  
 **Test before deployment:** Always test in a **controlled environment** before using in production.  
 **Keep logs secured:** Attackers may attempt to tamper with log files.  

---

## Troubleshooting

- **Permission Denied:** Run the script with `sudo`.
- **iptables/nftables not found:** Install using:
  ```bash
  sudo apt install iptables  # Debian/Ubuntu
  sudo yum install iptables  # CentOS/RHEL
  ```
- **Firewall rules not applying:** Verify with:
  ```bash
  sudo iptables -L -v -n
  ```
- **No logging output:** Ensure the script has write permissions to log files.

---

## Contributing

Contributions are welcome! Feel free to **open issues**, suggest improvements, or submit **pull requests**.

---
