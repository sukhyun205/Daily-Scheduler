from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)