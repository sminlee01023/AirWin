from flask import Flask,render_template

app = Flask(__name__)

# a = GetWeather()
# weather, temp = a.weather, a.temp
# a = GetDust()
# fine_dust, ultra_fine_dust = a.fine_dust_data, a.ultra_fine_dust_data

# socketio = SocketIO(app, logger=True, engineio_logger=True)

# async def time(websocket, path):
#     while True:
#         a = GetWeather()
#         weather, temp = a.weather, a.temp
#         a = GetDust()
#         fine_dust, ultra_fine_dust = a.fine_dust_data, a.ultra_fine_dust_data
#         await websocket.send(weather, temp, fine_dust, ultra_fine_dust)
#         await asyncio.sleep(60)

# start_server = websockets.serve(time, "127.0.0.1", 5000)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

@app.route("/")
def hello_world():
    return render_template('index.html')

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