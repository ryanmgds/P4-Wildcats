from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("main.html", food=food)

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')