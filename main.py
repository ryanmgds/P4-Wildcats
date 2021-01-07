from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Alabama.html')
def Alabama():
    return render_template("Alabama.html", alabama=alabama)

@app.route('/Alaska.html')
def Alaska():
    return render_template("Alaska.html", alaska=alaska)

@app.route('/Arizona.html')
def Arizona():
    return render_template("Arizona.html", arizona=arizona)

@app.route('/Arkansas.html')
def Arkansas():
    return render_template("Arkansas.html", arkansas=arkansas)

@app.route('/California.html')
def California():
    return render_template("California.html", california=california)

@app.route('/Colorado.html')
def Colorado():
    return render_template("Colorado.html", colorado=colorado)

@app.route('/Connecticut.html')
def Connecticut():
    return render_template("Connecticut.html", connecticut=connecticut)

@app.route('/Delaware.html')
def Delaware():
    return render_template("Delaware.html", delaware=delaware)

@app.route('/Florida.html')
def Florida():
    return render_template("Florida.html", florida=florida)

@app.route('/Georgia.html')
def Georgia():
    return render_template("Georgia.html", georgia=georgia)

@app.route('/Hawaii.html')
def Hawaii():
    return render_template("Hawaii.html", hawaii=hawaii)

@app.route('/Idaho.html')
def Idaho():
    return render_template("Idaho.html", idaho=idaho)

@app.route('/Illinois.html')
def Illinois():
    return render_template("Illinois.html", illinois=illinois)

@app.route('/Indiana.html')
def Indiana():
    return render_template("Indiana.html", indiana=indiana)

@app.route('/Iowa.html')
def Iowa():
    return render_template("Iowa.html", iowa=iowa)

@app.route('/Kansas.html')
def Kansas():
    return render_template("Kansas.html", kansas=kansas)

@app.route('/Kentucky.html')
def Kentucky():
    return render_template("Kentucky.html", kentucky=kentucky)

@app.route('/Louisiana.html')
def Louisiana():
    return render_template("Louisiana.html", louisiana=louisiana)

@app.route('/Maine.html')
def Maine():
    return render_template("Maine.html", maine=maine)

@app.route('/Maryland.html')
def Maryland():
    return render_template("Maryland.html", maryland=maryland)

@app.route('/Massachusetts.html')
def Massachusetts():
    return render_template("Massachusetts.html", massachusetts=massachusetts)

@app.route('/Michigan.html')
def Michigan():
    return render_template("Michigan.html", michigan=michigan)

@app.route('/Minnesota.html')
def Minnesota():
    return render_template("Minnesota.html", minnesota=minnesota)

@app.route('/Mississippi.html')
def Mississippi():
    return render_template("Mississippi.html", mississippi=mississippi)

@app.route('/Missouri.html')
def Missouri():
    return render_template("Missouri.html", missouri=missouri)

@app.route('/Montana.html')
def Montana():
    return render_template("Montana.html", montana=montana)

@app.route('/Nebraska.html')
def Nebraska():
    return render_template("Nebraska.html", nebraska=nebraska)

@app.route('/Nevada.html')
def Nevada():
    return render_template("Nevada.html", nevada=nevada)

@app.route('/NewHampshire.html')
def NewHampshire():
    return render_template("NewHampshire.html", newhampshire=newhampshire)

@app.route('/NewJersey.html')
def NewJersey():
    return render_template("NewJersey.html", newjersey=newjersey)

@app.route('/NewMexico.html')
def NewMexico():
    return render_template("NewMexico.html", newmexico=newmexico)

@app.route('/NewYork.html')
def NewYork():
    return render_template("NewYork.html", newyork=newyork)

@app.route('/NorthCarolina.html')
def NorthCarolina():
    return render_template("NorthCarolina.html", northcarolina=northcarolina)

@app.route('/NorhtDakota.html')
def NorthDakota():
    return render_template("NorthDakota.html", northdakota=northdakota)

@app.route('/Ohio.html')
def Ohio():
    return render_template("Ohio.html", ohio=ohio)

@app.route('/Oklahoma.html')
def Oklahoma():
    return render_template("Oklahoma.html", oklahoma=oklahoma)

@app.route('/Oregon.html')
def Oregon():
    return render_template("Oregon.html", oregon=oregon)

@app.route('/Pennsylvania.html')
def Pennsylvania():
    return render_template("Pennsylvania.html", pennsylvania=pennsylvania)

@app.route('/RhodeIsland.html')
def RhodeIsland():
    return render_template("RhodeIsland.html", rhodeisland=rhodeisland)

@app.route('/SouthCarolina.html')
def SouthCarolina():
    return render_template("SouthCarolina.html", southcarolina=southcarolina)

@app.route('/SouthDakota.html')
def SouthDakota():
    return render_template("SouthDakota.html", southdakota=southdakota)

@app.route('/Tennessee.html')
def Tennessee():
    return render_template("Tennessee.html", tennessee=tennessee)

@app.route('/Texas.html')
def Texas():
    return render_template("Texas.html", texas=texas)

@app.route('/Utah.html')
def Utah():
    return render_template("Utah.html", utah=utah)

@app.route('/Vermont.html')
def Vermont():
    return render_template("Vermont.html", vermont=vermont)

@app.route('/Virginia.html')
def Virginia():
    return render_template("Virginia.html", virginia=virginia)

@app.route('/Washington.html')
def Washington():
    return render_template("Washington.html", washington=washington)

@app.route('/WestVirginia.html')
def WestVirginia():
    return render_template("WestVirginia.html", westvirginia=westvirginia)

@app.route('/Wisconsin.html')
def Wisconsin():
    return render_template("Wisconsin.html", wisconsin=wisconsin)

@app.route('/Wyoming.html')
def Wyoming():
    return render_template("Wyoming.html", wyoming=wyoming)

@app.route('/main')
def main():
    return render_template("main.html", food=food)

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')