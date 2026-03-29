#  Cloud Threat Detection & Security Analytics System

##  Overview
This project simulates a cloud-based threat detection system that analyzes log data and identifies suspicious activities such as brute-force attacks, malicious IP access, and abnormal traffic patterns.

---

##  Architecture

Cloud Logs → Parser → Detection Engine → Threat Intelligence → Flask Dashboard

---

##  Features
- Brute-force attack detection  
-  DoS pattern detection  
-  Malicious IP identification  
-  Web-based dashboard (Flask)  
-  Alert deduplication  
-  Timestamp-based alert tracking  

---

##  Tech Stack
- Python  
- Flask  
- JSON (CloudTrail-style logs)  

---

##  How to Run

```bash
pip install flask
python app.py

##  Dashboard Preview
![Dashboard](dashboard.png)

---

##  Detection Engine Output
![Detection](detection.png)

---

##  Threat Intelligence Check
![Threat Intel](threat.png)
