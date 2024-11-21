from flask import Flask, render_template, request, jsonify
from core import get_Answer as gA

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-prompt', methods=['POST'])
def submit():
    user_prompt = request.form['user_prompt']
    response = gA(user_prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)