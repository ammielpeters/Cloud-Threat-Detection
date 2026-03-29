import json
import os

LOG_FILE = "logs/cloudtrail_logs.json"

def load_logs():
    try:
        # Check if file exists
        if not os.path.exists(LOG_FILE):
            raise FileNotFoundError(f"{LOG_FILE} not found")

        # Load JSON data
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

        # Validate structure
        if not isinstance(logs, list):
            raise ValueError("Invalid log format: Expected a list")

        return logs

    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format")
        return []

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return []

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return []