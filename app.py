from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_nearest_station_coor
import pygame

app = Flask(__name__)

@app.get("/")
def go_to_link():
    return render_template("index.html")
@app.get("/station/")
def get_register():
    pygame.mixer.init() #ChatGPT
    pygame.mixer.music.load("lofimusic.wav") #https://cloudconvert.com/mp3-to-wav after https://uppbeat.io/browse/trending
    pygame.mixer.music.play(-1)
    return render_template("station-form.html")


@app.post("/station/")
def post_register():
    place_name = str(request.form.get("location"))
    STOP, WHEELCHAIR = find_stop_near(place_name)
    return render_template("station-result.html", stop=STOP, wheelchair=WHEELCHAIR)


@app.route("/map")
def show_map():
    place_name = str(request.form.get("location"))
    LATITUDE, LONGITUDE = get_nearest_station_coor(place_name)
    html_map = f'<iframe src="https://maps.google.com/maps?q={LATITUDE},{LONGITUDE}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed" width="100%" height="500" frameboarder="0" style="border:0" allowfullscreen></iframe>' #ChatGPT
    return html_map


if __name__ == "__main__":
    app.run(debug=True, port=3640)
