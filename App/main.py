from flask import Flask, request, render_template_string
from datetime import datetime
import os

app = Flask(__name__)
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_filename():
    date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOG_DIR, f"{date_str}.log")

def get_next_log_number():
    filename = get_log_filename()
    if not os.path.exists(filename):
        return 1
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f) + 1

def write_log(f1, f2, f3):
    filename = get_log_filename()
    log_num = get_next_log_number()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Flask-service [#{log_num}] {f1.strip()} {f2.strip()} {f3.strip()}\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(entry)

def read_today_logs():
    filename = get_log_filename()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Field Logging App</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        input[type="text"] { width: 100%; margin-bottom: 10px; padding: 8px; }
        .log-entry { background: #f4f4f4; margin-top: 10px; padding: 10px; border-left: 5px solid #007BFF; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Multi-Field Logging App</h1>
    <form method="post">
        <input type="text" name="field1" placeholder="Field 1" required>
        <input type="text" name="field2" placeholder="Field 2" required>
        <input type="text" name="field3" placeholder="Field 3" required>
        <button type="submit">Submit Log</button>
    </form>

    <h2>Today's Logs</h2>
    {% for log in logs %}
        <div class="log-entry">{{ log }}</div>
    {% endfor %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f1 = request.form.get("field1", "")
        f2 = request.form.get("field2", "")
        f3 = request.form.get("field3", "")
        if f1 and f2 and f3:
            write_log(f1, f2, f3)
    logs = read_today_logs()
    return render_template_string(template, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
