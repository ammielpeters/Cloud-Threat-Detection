# Simulated Threat Intelligence Database

MALICIOUS_IPS = [
    "45.33.32.156",  # suspicious external IP
    "10.0.0.5"       # internal compromised host (example)
]

def is_malicious(ip):
    return ip in MALICIOUS_IPS