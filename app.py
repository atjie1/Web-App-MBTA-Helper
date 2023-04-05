from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_nearest_station_coor

app = Flask(__name__)


@app.route("/")
def get_map():
    return render_template("index.html")


ACTIONS = ["Show Map"]


@app.get("/station/")
def get_register():
    return render_template("station-form.html", courses=ACTIONS)


@app.post("/station/")
def post_register():
    action = request.form.get("action")
    # if course not in ACTIONS:
    #     return render_template("failure.html")
    if action == "Show Map":
        return show_map()
    place_name = str(request.form.get("location"))
    STOP, WHEELCHAIR = find_stop_near(place_name)
    return render_template("station-result.html", stop=STOP, wheelchair=WHEELCHAIR)


@app.route("/map")
def show_map():
    place_name = str(request.form.get("location"))
    LATITUDE, LONGITUDE = get_nearest_station_coor(place_name)
    html_map = f'<iframe src="https://maps.google.com/maps?q={LATITUDE},{LONGITUDE}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>'
    return html_map


if __name__ == "__main__":
    app.run(debug=True, port=3640)
