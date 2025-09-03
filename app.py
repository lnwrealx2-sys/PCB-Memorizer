from flask import Flask,render_template,jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    folder_path_B = 'static/BQuest'
    filesB = os.listdir(folder_path_B)
    fileB_count = len(filesB)-1
    folder_path_P = 'static/PQuest'
    filesP = os.listdir(folder_path_P)
    fileP_count = len(filesP)-1
    folder_path_C = 'static/CQuest'
    filesC = os.listdir(folder_path_C)
    fileC_count = len(filesC)-1

    return render_template('index.html', fileP=fileP_count, fileB=fileB_count, fileC=fileC_count)

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "message": "Internal Server Error",
        "error": str(error)
    }), 500

if __name__ == '__main__':

    app.run(debug=True)

