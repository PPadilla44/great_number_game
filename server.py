from flask import Flask, redirect, session, render_template, request
import random
app = Flask(__name__)
app.secret_key = 'bleh'
@app.route('/')
def index():
    if not 'users' in session:
        session['users']=[]
    if 'guess' in session:
        session.pop('guess')
    session['attempts'] = 0
    session['great_num'] = random.randint(1, 100)
    return render_template("index.html")
@app.route("/guess", methods=["POST"])
def show():
    session['guess'] = int(request.form['guess'])
    session['attempts']+=1
    print(session['great_num'])
    return render_template("show.html")
@app.route("/leaderboard", methods=["POST"])
def winners():
    final_attempt = session['attempts']
    form_name = request.form['name']
    session['user'] = {'name' : form_name, 'attempt' : final_attempt}
    session['users'].append(session['user'])
    return render_template("leaderboard.html")
if __name__ == "__main__":
    app.run(debug=True)
