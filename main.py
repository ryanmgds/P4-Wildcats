from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/healthylunches')
def datatable():
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

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')

# @app.route('/scrubbing')
# def scrubbing():
#       url = 'https://covid.cdc.gov/covid-data-tracker/#cases_totalcases'
#       r = requests.get(url)
#       soup = BeautifulSoup(r.text, 'html.parser')
#       print(soup)
#       return render_template("home.html")
