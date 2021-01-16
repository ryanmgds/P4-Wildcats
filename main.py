from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')
