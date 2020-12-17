from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():

    food = [
        {
            "name":"Salad",
            "price":5
        },

        {
            "name":"Pizza",
            "price":13
        },

        {
            "name":"Club Sandwiches",
            "price":9
        },

        {
            "name":"Pasta",
            "price":11
        },
    ]
    return render_template("main.html", food=food)



if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')
