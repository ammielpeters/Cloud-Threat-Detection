from collections import defaultdict
from threat_intel import is_malicious

def detect_threats(logs):
    alerts = []
    seen = set()
    failed_attempts = defaultdict(int)
    request_count = defaultdict(int)

    for log in logs:
        ip = log.get("sourceIPAddress")
        event = log.get("eventName")
        response = log.get("response")

        if not ip or not event or not response:
            continue

        request_count[ip] += 1

        # Brute Force Detection
        if event == "ConsoleLogin" and response == "Failed":
            failed_attempts[ip] += 1

            if failed_attempts[ip] >= 3:
                alert_key = (ip, "Brute Force Attack")

                if alert_key not in seen:
                    alerts.append({
                        "ip": ip,
                        "type": "Brute Force Attack",
                        "severity": "High",
			"time": log.get("eventTime")
                    })
                    seen.add(alert_key)

        # DoS Detection
        if request_count[ip] > 5:
            alert_key = (ip, "Potential DoS Activity")

            if alert_key not in seen:
                alerts.append({
                    "ip": ip,
                    "type": "Potential DoS Activity",
                    "severity": "Medium",
		    "time": log.get("eventTime")
                })
                seen.add(alert_key)

        # Threat Intelligence
        if is_malicious(ip):
            alert_key = (ip, "Known Malicious IP")

            if alert_key not in seen:
                alerts.append({
                    "ip": ip,
                    "type": "Known Malicious IP",
                    "severity": "High",
		    "time": log.get("eventTime")
                })
                seen.add(alert_key)

    return alerts