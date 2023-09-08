from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

app.json.sort_keys = False
app.config["DEBUG"] = True

CORS(app)

@app.route('/api', methods=["GET"])
def return_details():
    if request.method == "GET":
        slack_name = request.args.get("slack_name", None)
        track = request.args.get("track", None)
    
        res = {
            "slack_name": slack_name,
            "current_day": datetime.now().strftime("%A"),
            "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "https://github.com/datalordstephen/hng-task-1/blob/master/main.py",
            "github_repo_url": "https://github.com/datalordstephen/hng-task-1",
            "status_code": 200
        }
        
        return jsonify(res)