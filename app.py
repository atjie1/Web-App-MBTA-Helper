from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/MBTA_Helper')

@app.get('/MBTA_Helper')
def get_MBTA():
    return render_template('index.html')

@app.post('/MBTA_stop')
def MBTA_Helper():
    place_name = request.form.get('location')
    stop = find_stop_near(place_name)
    return render_template('index.html', location=place_name, stop=stop)

if __name__ == '__main__':
    app.run(debug=True)
