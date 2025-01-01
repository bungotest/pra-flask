from flask import Flask, render_template, request, redirect

app=Flask(__name__)

players = [
    {'id': 1, 'name': 'Joey', 'age': 12, 'image': 'Joey.jpg'},
    {'id': 2, 'name': 'JazG', 'age': 14, 'image': 'JazG.jpg'},
    {'id': 3, 'name': 'Rose', 'age': 16, 'image': 'Rose.jpg'},
    {'id': 4, 'name': 'Joy', 'age': 11, 'image': 'Joy.jpg'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players',methods=['GET','POST'])
def player_list():
    if request.method =='GET':
        return render_template('players.html', players=players)
    
@app.route('/players/<int:player_id>')
def player_detail(player_id):
    player = next((p for p in players if p['id'] == player_id), None)
    if player:
        return render_template('player_detail.html', player=player)
    else:
        return redirect ('index.html')   

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)