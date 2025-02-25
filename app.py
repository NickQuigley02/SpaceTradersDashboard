from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv


load_dotenv()

AGENT_TOKEN = os.getenv("AGENT_TOKEN")


app = Flask(__name__)







def get_agent_data():
	MyAgentURL = "https://api.spacetraders.io/v2/my/agent"

	headers = {
	    "Authorization": f"Bearer {AGENT_TOKEN}"
	}

	AgentResponse = requests.get(MyAgentURL, headers=headers)
	if AgentResponse.status_code == 200:
		print(AgentResponse.json().get('data', {}))
		return AgentResponse.json().get('data', {})
	else:
        	return {"error": f"API Error: {response.status_code}"}




@app.route('/')
def dashboard():
	"""Renders the dashboard with agent data."""
	return render_template("dashboard.html", agent=get_agent_data())

if __name__ == '__main__':
	app.run(debug=True)

