from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/quickpow", methods=['GET', 'POST'])
def pow_calc():
    if request.method == 'GET':
        result = None
    else:
        base_value = int(request.form["base_value"])
        pow_value = int(request.form["pow_value"])
        mod_value = int(request.form["mod_value"])
        result = quick_pow(base_value, pow_value, mod_value)
    return render_template("pow.html", result=result)


@app.route("/rabin", methods=['GET', 'POST'])
def rabin():
    if request.method == 'GET':
        result = None
    else:
        p_value = int(request.form["p_value"])
        q_value = int(request.form["q_value"])
        c_value = int(request.form["c_value"])
        result = calculate(p_value, q_value, c_value)
    return render_template("rabin.html", result=result)


@app.route("/euklid", methods=['GET', 'POST'])
def find_euklid():
    if request.method == 'GET':
        result = None
    else:
        base_value = int(request.form["base_value"])
        mod_value = int(request.form["mod_value"])
        result = euklid(base_value, mod_value)
    return render_template("euklid.html", result=result)
