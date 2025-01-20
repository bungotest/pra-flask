from flask import Flask, render_template, request, redirect # type: ignore
from wtforms import StringField, Form, SubmitField, IntegerField, PasswordField, DateField, RadioField, BooleanField # type: ignore
from wtforms.form import Form # type: ignore
import os


app=Flask(__name__)

app.config['SECRET_KEY']="mysecretkey"
print(os.urandom(16))

players = [
    {'id': 1, 'name': 'Joey', 'age': 12, 'image': 'Joey.jpg'},
    {'id': 2, 'name': 'JazG', 'age': 14, 'image': 'JazG.jpg'},
    {'id': 3, 'name': 'Rose', 'age': 16, 'image': 'Rose.jpg'},
    {'id': 4, 'name': 'Joy', 'age': 11, 'image': 'Joy.jpg'},
]

class UserForm(Form): 
    name=StringField('Name')
    age=IntegerField('Age')
    password=PasswordField('Password')
    birthday=DateField('Birthday')
    gender=RadioField('Gender', choices=[('man','male'), ('woman','Female')])
    experience=BooleanField('Have Experience?')
    submit=SubmitField('Submit')

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

@app.route('/form_registration' ,methods=['GET', 'POST'])
def registration_form():
    name = age = password = birthday = gender = experience = ''
    form=UserForm(request.form)
    if request.method == "POST":
        if form.validate():
            name=form.name.data
            age=form.age.data
            password=form.password.data
            birthday=form.birthday.data
            gender=form.gender.data
            experience=form.experience.data
            submit=form.submit.data
            form=UserForm()
            print('登録完了しました')
            print(form.name())
        else :
            print('違います')
    return render_template('form_registration.html', form=form, name=name, age=age, password=password, birthday=birthday, gender=gender, experience=experience)


if __name__ == '__main__':
    app.run(debug=True)