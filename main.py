from flask import Flask, render_template, request, redirect

import smtplib

# from bs4 BeautifulSoup import

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

 @app.route('/scrubbing')
 def scrubbing():
     url = 'https://covid.cdc.gov/covid-data-tracker/#cases_totalcases'
     r = requests.get(url)
     soup = BeautifulSoup(r.text, 'html.parser')
     print(soup)
     return render_template("home.html")

@app.route('/email', methods = ['POST'])
def email():
    email = request.form['email']
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('wildcatsp4@gmail.com', 'MrMadman33')
    server.sendmail('wildcatsp4@gmail.com', email, "California Total Cases = 29324890u123")
    server.close()
    print ("email sent to:", email)
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')
