from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "callBack"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

app.run(debug = True)