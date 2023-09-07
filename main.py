from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/api")
def return_details(slack_name: str, track: str):
    res = {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime("%A"),
        "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/datalordstephen/hng-task-1/blob/master/main.py",
        "github_repo_url": "https://github.com/datalordstephen/hng-task-1",
        "status_code": 200
    }
    
    return res