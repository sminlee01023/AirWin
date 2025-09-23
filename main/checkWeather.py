from flask import session 
from flask_socketio import emit
from croll import GetWeather, GetDust

a = GetWeather()
weather, temp = a.weather, a.temp
a = GetDust()
fine_dust, ultra_fine_dust = a.fine_dust_data, a.ultra_fine_dust_data

def socketio_init(socketio):
    @socketio.on('testSocket',namespace='/test')
    def testEvent(message):
        tsession = session.get('test')
        print('received message'+str(message))
        retMessage = { 'msg' : "hello response" }
        emit('test',retMessage,callback=tsession)