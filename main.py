from flask import Flask, render_template, request, redirect

import smtplib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/email', methods = ['POST'])
def email():
    email = request.form['email']
    email_text = 'Subject: {}\n\n{}'.format("California Total Cases", 'California Total Cases 2,816,969')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('wildcatsp4@gmail.com', 'MrMadman33')
    server.sendmail('wildcatsp4@gmail.com', email, email_text)
    server.close()
    print ("email sent to:", email)
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')
