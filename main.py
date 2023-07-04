from flask import Flask, render_template, request
from newFunctions import *

app = Flask('The Great McDonalds Battle', static_folder='static', template_folder="templates")


# Present the user with an introduction of the project and the button to start the game
@app.route('/', methods=["GET", "POST"])
def home():
  endGame()
  return render_template('index.html')

# This is where the user makes the choice to either run away or fight Karen
@app.route('/battle', methods=["GET", "POST"])
def battle():
  bothHealth = getHealth()
  if(int(bothHealth["yourHealth"]) <= 0):
    endGame()
    return render_template("youdied.html")
  return render_template('battle.html', data = bothHealth)

@app.route('/attack', methods=["GET", "POST"])
def results():
  #userpicked = str(request.form.get('choice'))
  #if(userpicked == "engage"):
    #attackData = attack()
    #return render_template('attack.html', data = attackData)
  #if(userpicked == "run"):
    #return render_template("runaway.html", data = userpicked)
  attackData = attack()
  return render_template("attack.html", data = attackData)

@app.route("/runaway", methods=["GET", "POST"])
def runaway():
  chance = random.randrange(101)
  if chance >= 50:
    return render_template("successrunaway.html")
  elif chance <= 49:
    return render_template("failrunaway.html")

@app.route("/restart", methods=["GET", "POST"])
def restart():
  endGame()
  return render_template("restart.html")

@app.route("/attacked", methods=["GET", "POST"])
def attacked():
  bothHealth = getHealth()
  if(int(bothHealth["karenHealth"]) <= 0):
    endGame()
    return render_template("karendied.html")
  attackedData = enemyStrike()
  return render_template("attacked.html", data = attackedData)

app.run(host='0.0.0.0', port=6969, threaded=True)