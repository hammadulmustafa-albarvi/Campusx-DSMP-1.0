from flask import Flask,render_template,request
import requests
app = Flask(__name__)


@app.route("/")
def homepage():
    result = requests.get("http://127.0.0.1:5000/api/teams")
    ans = result.json()['teams']
    return render_template('homepage.html',ans=ans)



@app.route("/teamvsteam")
def teamvteam():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    data = requests.get(f"http://127.0.0.1:5000/api/teams_vs_team?team1={team1}&team2={team2}")
    response = data.json()
    result1 = requests.get("http://127.0.0.1:5000/api/teams")
    ans = result1.json()['teams']
    print(team1,team2)
    return render_template('homepage.html',result=response,ans=ans)


app.run(debug=True,port=7000) 




# http://127.0.0.1:5000/api/teams_vs_team?team1={team1}&team2={team2}
# http://127.0.0.1:5000/api/teams