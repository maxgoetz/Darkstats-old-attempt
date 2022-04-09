from flask import Flask, render_template, request, redirect

import os

from helpers import Player, add



app: Flask = Flask(__name__)

player: list[str] = []

player_list: list[Player] = []

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/players', methods=["GET", "POST"])
def players():
    if request.method == "POST":
        global player
        player = request.form.getlist('players')
        
        for p in player:
            new_player: Player = Player(f"{p}")
            player_list.append(new_player)

        # return redirect("/stats")
        return render_template('/success.html')
        
    return render_template('create-todo.html')


@app.route('/stats', methods=["GET", "POST"])
def create_todo() -> None:
    if request.method == "POST":
        #selected = request.form("selected")
        if request.form['stat'] == 'Drops':
            for liner in player_list:
                if liner.name == request.form("selected"):
                    liner.drops += 1
                    print(liner.drops)
                                
        # if request.form['stat'] == 'Turnover':

        # if request.form['stat'] == 'Assist':

        # if request.form['stat'] == 'Block':

        # if request.form['stat'] == 'Score':
        #     return render_template('index.html')
    return render_template('create-todo.html')
    

    # return render_template("success.html", player=player)


# @app.route('/stats', methods=["GET", "POST"])
# def record_score():

#     return render_template('success.html',  player=player)

if __name__ == '__main__':
    app.run(debug=True)