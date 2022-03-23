from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)
application = app

players_list = convert_to_dict("players.csv")

pairs_list = []
for p in players_list:
    pairs_list.append( (p['ID'], p['Name']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="NBA All Time Leaders")

@app.route('/player/<num>')
def detail(num):
    try:
        player_dict = players_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Player: {num}</h1>"
    return render_template('player.html', player=player_dict, the_title=player['Name'])

if __name__ == '__main__':
    app.run(debug=True)
