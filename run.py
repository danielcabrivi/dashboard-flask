from flask import Flask, render_template
import processamento
from datetime import date, datetime

app = Flask(__name__)

@app.route('/')
def home():
    describe = processamento.getDescribe()
    head = processamento.getDataHead(5)
    data = [describe, head]

    return render_template("dashboard.html", dados=data)

@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/icons')
def icons():
    return render_template("icons.html")

app.run(port=5400, debug=True)