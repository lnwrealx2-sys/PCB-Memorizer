from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():

    return 'ควยasdk;jasd;kj;kj;k'


if __name__ == '__main__':

    app.run(debug=True)






