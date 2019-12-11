from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/word', methods=['GET'])
def word():
    words = ['hello', 'world']
    redirect = url_for('result')
    return render_template('showData.html', words = words, len= len(words), redirect = redirect)

@app.route('/sentence')
def sentence():
    words = ['hello', 'world']
    return render_template('showData.html', words = words, len= len(words))

@app.route('/result')
def result():
    result = 92.87
    return render_template('results.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)