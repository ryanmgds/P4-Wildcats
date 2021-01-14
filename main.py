from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Alabama.html')
def alabama():
    return render_template("alabama.html", alabama=alabama)


@app.route('/Alaska.html')
def alaska():
    return render_template("Alaska.html", alaska=alaska)


@app.route('/Arizona.html')
def arizona():
    return render_template("Arizona.html", arizona=arizona)


@app.route('/Arkansas.html')
def arkansas():
    return render_template("Arkansas.html", arkansas=arkansas)


@app.route('/California.html')
def california():
    return render_template("California.html", california=california)


@app.route('/Colorado.html')
def colorado():
    return render_template("Colorado.html", colorado=colorado)


@app.route('/Connecticut.html')
def connecticut():
    return render_template("Connecticut.html", connecticut=connecticut)


@app.route('/Delaware.html')
def delaware():
    return render_template("Delaware.html", delaware=delaware)


@app.route('/Florida.html')
def florida():
    return render_template("Florida.html", florida=florida)


@app.route('/Georgia.html')
def georgia():
    return render_template("Georgia.html", georgia=georgia)


@app.route('/Hawaii.html')
def hawaii():
    return render_template("Hawaii.html", hawaii=hawaii)


@app.route('/Idaho.html')
def idaho():
    return render_template("Idaho.html", idaho=idaho)


@app.route('/Illinois.html')
def illinois():
    return render_template("Illinois.html", illinois=illinois)


@app.route('/Indiana.html')
def indiana():
    return render_template("Indiana.html", indiana=indiana)


@app.route('/Iowa.html')
def iowa():
    return render_template("Iowa.html", iowa=iowa)


@app.route('/Kansas.html')
def kansas():
    return render_template("Kansas.html", kansas=kansas)


@app.route('/Kentucky.html')
def kentucky():
    return render_template("Kentucky.html", kentucky=kentucky)


@app.route('/Louisiana.html')
def louisiana():
    return render_template("Louisiana.html", louisiana=louisiana)


@app.route('/Maine.html')
def maine():
    return render_template("Maine.html", maine=maine)


@app.route('/Maryland.html')
def maryland():
    return render_template("Maryland.html", maryland=maryland)


@app.route('/Massachusetts.html')
def massachusetts():
    return render_template("Massachusetts.html", massachusetts=massachusetts)


@app.route('/Michigan.html')
def michigan():
    return render_template("Michigan.html", michigan=michigan)


@app.route('/Minnesota.html')
def minnesota():
    return render_template("Minnesota.html", minnesota=minnesota)


@app.route('/Mississippi.html')
def mississippi():
    return render_template("Mississippi.html", mississippi=mississippi)


@app.route('/Missouri.html')
def missouri():
    return render_template("Missouri.html", missouri=missouri)


@app.route('/Montana.html')
def montana():
    return render_template("Montana.html", montana=montana)


@app.route('/Nebraska.html')
def nebraska():
    return render_template("Nebraska.html", nebraska=nebraska)


@app.route('/Nevada.html')
def nevada():
    return render_template("Nevada.html", nevada=nevada)


@app.route('/NewHampshire.html')
def newhampshire():
    return render_template("NewHampshire.html", newhampshire=newhampshire)


@app.route('/NewJersey.html')
def newjersey():
    return render_template("NewJersey.html", newjersey=newjersey)


@app.route('/NewMexico.html')
def newmexico():
    return render_template("NewMexico.html", newmexico=newmexico)


@app.route('/NewYork.html')
def newyork():
    return render_template("NewYork.html", newyork=newyork)


@app.route('/NorthCarolina.html')
def northcarolina():
    return render_template("NorthCarolina.html", northcarolina=northcarolina)


@app.route('/NorhtDakota.html')
def northdakota():
    return render_template("NorthDakota.html", northdakota=northdakota)


@app.route('/Ohio.html')
def ohio():
    return render_template("Ohio.html", ohio=ohio)


@app.route('/Oklahoma.html')
def oklahoma():
    return render_template("Oklahoma.html", oklahoma=oklahoma)


@app.route('/Oregon.html')
def oregon():
    return render_template("Oregon.html", oregon=oregon)


@app.route('/Pennsylvania.html')
def pennsylvania():
    return render_template("Pennsylvania.html", pennsylvania=pennsylvania)


@app.route('/RhodeIsland.html')
def rhodeisland():
    return render_template("RhodeIsland.html", rhodeisland=rhodeisland)


@app.route('/SouthCarolina.html')
def southcarolina():
    return render_template("SouthCarolina.html", southcarolina=southcarolina)


@app.route('/SouthDakota.html')
def southdakota():
    return render_template("SouthDakota.html", southdakota=southdakota)


@app.route('/Tennessee.html')
def tennessee():
    return render_template("Tennessee.html", tennessee=tennessee)


@app.route('/Texas.html')
def texas():
    return render_template("Texas.html", texas=texas)


@app.route('/Utah.html')
def utah():
    return render_template("Utah.html", utah=utah)


@app.route('/Vermont.html')
def vermont():
    return render_template("Vermont.html", vermont=vermont)


@app.route('/Virginia.html')
def virginia():
    return render_template("Virginia.html", virginia=virginia)


@app.route('/Washington.html')
def washington():
    return render_template("Washington.html", washington=washington)


@app.route('/WestVirginia.html')
def westvirginia():
    return render_template("WestVirginia.html", westvirginia=westvirginia)


@app.route('/Wisconsin.html')
def wisconsin():
    return render_template("Wisconsin.html", wisconsin=wisconsin)


@app.route('/Wyoming.html')
def wyoming():
    return render_template("Wyoming.html", wyoming=wyoming)


@app.route('/main')
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')
