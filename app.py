from flask import Flask, render_template
import json
from parser import load_logs
from detector import detect_threats

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Load logs
    logs = load_logs()

    # Detect threats
    alerts = detect_threats(logs)

    # Save alerts to file (for persistence)
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)

    # Send alerts to UI
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)