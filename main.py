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

@app.route('/healthylunches')
def healthylunches():

    lunches = [
        {
            "name":"Chicken Parmesian",
            "price":10
        },

        {
            "name":"Chicken Stir Fry",
            "price":15
        },
    ]

    if request.method == 'POST':
        lunches.append({
            "name":request.form["name"],
            "price":request.form["price"]
        })

    return render_template("healthylunches.html", lunches=lunches)


@app.route('/othershopping')
def othershopping():

    shopping = [
        {
            "name":"CS Jokes",
            "price":0
        },

        {
            "name":"CS Videos",
            "price":0
        },
    ]


    return render_template("othershopping.html", shopping=shopping)


@app.route('/tastydesserts', methods=['GET', 'POST'])
def tastydesserts():

    desserts = [
        {
            "name":"cheesecake",
            "price":10
        },

        {
            "name":"ice cream",
            "price":15
        },
    ]

    if request.method == 'POST':
        desserts.append({
            "name":request.form["name"],
            "price":request.form["price"]
        })

    return render_template("tastydesserts.html", desserts=desserts)


@app.route('/healthydinners')
def healthydinners():

    dinners = [
        {
            "name": "steak: $15",
            "price": 15
        },

        {
            "name": "soup: $11",
            "price": 11
        }
    ]
    return render_template("healthydinners.html", dinners=dinners)

@app.route('/shoppingbag')
def shoppingbag():


    if request.method == 'POST':
        shoppingbag.append({
            "name":request.form["name"],
            "quantity":request.form["quantity"]
        })

    return render_template("shoppingbag.html", shoppingbag = shoppingbag)

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')
