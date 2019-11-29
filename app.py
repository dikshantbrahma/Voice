from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    words
    return render_template('index.html', words= words )

if __name__ == '__main__':
    app.run(debug=True)