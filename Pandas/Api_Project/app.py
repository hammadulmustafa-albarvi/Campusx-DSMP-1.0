from flask import Flask,jsonify,request
from ipl import *
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"


@app.route("/api/teams")
def teams():
    teams = teamApi()
    return jsonify(teams)

@app.route('/api/teams_vs_team',methods=['get'])
def teams_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    result = teamvsteam(team1,team2)
    return jsonify(result)


@app.route('/api/teamdata',methods=['get'])
def teamdata():
    team = request.args.get('team2')
    result = team_data(team)
    return jsonify(result)

app.run(debug=True)
