from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.get("/station") #METHOD NOT ALLOWED #Attribute error
def get_station():
    return render_template("station-form.html")

@app.post('/station')
def stop_post():
    place_name = request.form.get('location')
    place_name = str(place_name)
    stop, wheelchair = find_stop_near(place_name)
    return render_template('station-result.html', stop=stop, wheelchair=wheelchair)
    

if __name__ == "__main__":
    app.run(debug=True, port=3640)
