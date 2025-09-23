from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import time

'''
a = GetDust()
degree, condition = a.ultra_fine_dust_data

형식으로 data 가져올 수 있음
'''

class GetWeather:
    def get_data():
        html = requests.get('https://weather.naver.com/today/11185763')
        soup = bs(html.text,'html.parser')

        raw_data = soup.find('div',{'class':'weather_area'})

        raw_temp_data = raw_data.find('strong', {'class': 'current'})
        raw_weather_data = raw_data.find('span', {'class': 'weather'})

        temp = raw_temp_data.get_text()[6:-2]
        weather = raw_weather_data.get_text()

        return temp, weather

    temp, weather = get_data()


class GetDust:
    def get_data():
        html = requests.get('https://weather.naver.com/air/11185761')
        soup = bs(html.text,'html.parser')

        raw_data = soup.find('div',{'class':'top_area'})

        raw_dust_data = raw_data.find_all('em')

        fine_dust_data = raw_dust_data[0].get_text().split('\n')[1:3]
        ultra_fine_dust_data = raw_dust_data[1].get_text().split('\n')[1:3]

        return fine_dust_data, ultra_fine_dust_data  

    fine_dust_data, ultra_fine_dust_data = get_data()   
