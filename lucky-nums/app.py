from flask import Flask, json, render_template, jsonify, request
import requests
from random import randint
app = Flask(__name__)


errors = {
    'color': 'Invalid value, must be one of: red, green, orange, blue.',
    'name': 'Name is required',
    'email': 'Email is required',
    'year': 'Year is required',
}
name = request.form['name']
email = request.form['email']
year = request.form['year']
color = request.form['color']
luck_num = randint(1, 100)
number_req = requests.get(f'http://numbersapi.com/{luck_num}')
num_fact = str(number_req.text)
result = {'num': {
    'fact': f'{num_fact}',
    'num': f'{luck_num}'
},
    'year': {
    'fact': f'{year} is the year nothing remarkable happened',
    'year': f'{year}'}
}


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html", errors=errors, result=result)


@app.route('/api/get-lucky-num/', methods=['POST'])
def lucky_num():

    if name and email and year and color != '':
        return jsonify(result)
    if name is '':
        return jsonify(errors['name'])
    if email is '':
        return jsonify(errors['email'])
    if year is '':
        return jsonify(errors['year'])
    if color is '':
        return jsonify(errors['color'])
