from flask import Flask,render_template
from croll import GetWeather, GetDust
from flask_socketio import SocketIO, send
from checkWeather import socketio_init
import asyncio
import websockets
import numpy as np

app = Flask(__name__)

@app.route("/")
def first():
    return render_template('first.html')

@app.route("/login")
def login():
    return render_template('/login.html')

@app.route("/register")
def register():
    return render_template('/register.html')

@app.route("/main")
def hello_world():
    a = GetWeather()
    weather, temp = a.weather, a.temp
    a = GetDust()
    [fine_dust_level, fine_dust_grade], [ultra_fine_dust_level, ultra_fine_dust_grade] = a.fine_dust_data, a.ultra_fine_dust_data
    return render_template('main_content.html', indoor_dust = np.random.randint(15, 100), weather = weather, temp = temp, 
        fine_dust_level = fine_dust_level, fine_dust_grade = fine_dust_grade, ultra_fine_dust_level = ultra_fine_dust_level, ultra_fine_dust_grade = ultra_fine_dust_grade)

@app.route("/flash")
def hello_world2():
    return render_template('flash_video.html')

@app.route("/inventory")
def hello_world3():
    return render_template('inventory.html')

# @socketio.on('data')
# def request(t):
#     to_client = dict()
#     while True:
#         a = GetWeather()
#         to_client['weather'], to_client['temp'] = a.weather, a.temp
#         a = GetDust()
#         to_client['fine_dust'], to_client['ultra_fine_dust'] = a.fine_dust_data, a.ultra_fine_dust_data
#         send(to_client, broadcast=True)

if __name__ == '__main__':
    app.debug = True
    app.run()
    # socketio.run(app, debug=True, port=5000)