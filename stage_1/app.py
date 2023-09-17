from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # user provided parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    #date time parameters
    current_day = datetime.now().strftime('%A')
    utc_now = datetime.now().strftime('%Y-%m-%dT%XZ')
    
    #response parameters
    response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_now,
            "track": track,
            "github_file_url": "https://github.com/babashehu01/HNGx/blob/main/app.py",
            "github_repo_url": "https://github.com/babashehu01/HNGx",
            "status_code": 200
    }

    return jsonify(response)
