# mac_changer
# 🔧 MAC Changer Tool – Python Networking Project

A simple Python-based command-line tool to spoof (change) your MAC address on Linux systems. Built as a final-year project to understand system-level scripting and ethical hacking basics.

---

## 🚀 Features

- ✅ View current MAC address
- ✅ Change MAC to custom or random
- ✅ Verify if the change was successful
- ✅ Lightweight & Linux CLI friendly

---

## 📸 Screenshots

<img width="559" height="203" alt="Screenshot 2025-07-24 201254" src="https://github.com/user-attachments/assets/7ecf58f0-52f5-4b60-ac61-70897e51dfa4" />

---

## 💻 Technologies Used

- Python 3
- subprocess, optparse, regex, random
- Linux (`ifconfig` command)

---

## 📜 Usage

```bash
# Change MAC manually
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55

# Generate and apply random MAC
sudo python3 mac_changer.py -i wlan0 -r
