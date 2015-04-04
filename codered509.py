from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/")
def chooseCoords():
    return render_template("chooseCoords.html")

@app.route("/targetcoords", methods=["GET","POST"])
def targetCoords():
    if request.method == "POST":
        return "test"

@app.route("/maptest")
def mapTest():
    return render_template("mapsTest.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
