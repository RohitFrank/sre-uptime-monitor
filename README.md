# 🔍 Simple SRE Uptime Monitor

This is a lightweight Python script that monitors whether a website is UP or DOWN at regular intervals. It simulates the kind of basic monitoring tasks performed by Site Reliability Engineers (SREs).

---

## 🚀 Features
- Sends periodic HTTP GET requests to a specified URL
- Logs whether the website is UP or DOWN
- Prints timestamped status messages
- Easy to run, customize, and expand

---

## 📦 Technologies Used
- Python 3
- requests library
- Git & GitHub

---

## 📂 File Structure
simple-sre-uptime-monitor/
├── monitor.py      # Main monitoring script
└── README.md       # Project description and instructions

---

## 🧪 How to Run

1. Clone the Repository
   git clone https://github.com/RohitFrank/sre-uptime-monitor.git
   cd sre-uptime-monitor

2. Install Required Library
   pip install requests

3. Run the Monitor
   python monitor.py

---

## 🖥️ Sample Output
Sat Jun 14 14:35:21 2025: https://google.com is UP  
Sat Jun 14 14:35:51 2025: https://google.com is UP  
Sat Jun 14 14:36:21 2025: https://google.com is DOWN. Failed to connect.

---

## 💡 Why This Project?

This project helps beginners and aspiring SREs understand the basics of monitoring and reliability. It’s a small script with real-world relevance, great for:
- Mini projects
- Portfolio work
- Interview discussions

---

## 🔧 Possible Upgrades
- Monitor multiple URLs
- Log output to a file
- Send email/Slack alerts on failures
- Run as a background service or Docker container

---

👨‍💻 Created by Rohit Francis — feel free to fork, star, or contribute!
add full README content

