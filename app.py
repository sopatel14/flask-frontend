from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    response = requests.post("http://backend:5000/api/submit", json={"name": name})
    return f"Response from backend: {response.json()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
