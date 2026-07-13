# ⚡ KYSA-Lookup: Advanced Terminal OSINT & Recon Engine

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Status-Active_Development-orange.svg)

KYSA-Lookup is a powerful, lightweight, terminal-based Open Source Intelligence (OSINT) and reconnaissance engine written in Python. Designed with a clean, responsive hacker-style ANSI interface, it allows security enthusiasts and researchers to run quick footprint audits and live network lookups from a single console.

> **Note:** This project is under active, daily development as I advance through my computer science and backend engineering journey.

---

## 🚀 Core Features

The tool is split into modular forensics blocks, combining local parsing mechanics with live network API queries:

* 📱 **Phone Intelligence:** Extracts structural E.164 identity formatting, carrier identification, and regional timezones.
* 🌐 **Global Username Scanner:** Scans live global platforms (GitHub, Reddit, Twitch, and more) simultaneously to map an alias footprint.
* 🗺️ **Threat IP Geolocation:** Connects to live network routing databases to trace server nodes to their approximate city/region footprint.
* 🔍 **DNS & Domain Resolver:** Uses native socket layers to map active corporate domain root networks down to physical hosting servers.
* 🖼️ **EXIF Metadata Reader:** Extracts hidden device and hardware profile logs embedded inside local image files.

---

## 🛠️ Installation & Setup

Clone the repository and install the minimal dependencies required for the local processing modules:

```bash
# Clone the repository
git clone [https://github.com/flxansh/kysa-lookup.git](https://github.com/flxansh/kysa-lookup.git)

# Navigate into the project folder
cd kysa-lookup

# Install required dependencies
pip install phonenumbers Pillow
