import time
import requests
import random
from bs4 import BeautifulSoup
import csv
import sqlite3

url = 'https://gulf.ge/ge/fuel_prices?fbclid=IwAR2ymxUmGx4CHxWH5DQMxV3nPgPK_0bqpB6x_5_lLq0ejtp2VF3Ku3YVZJE&page=1'
payload = {'page': 1}
h = {'Accept-Language': 'en-US'}
conn = sqlite3.connect('Petrol.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Petrol
( 
  Date TEXT,
  G_Force_Super REAL,
  G_Force_Premium REAL,
  G_Force_Euro_Regular REAL,
  Euro_Regular REAL,
  G_Force_Euro_Diesel REAL,
  Euro_Diesel REAL,
  Fuel_Gas REAL
)''')

file = open('Petrol.csv', 'w', newline='\n', encoding='UTF-8-sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['თარიღი', 'G-Force სუპერი', 'G-Force პრემიუმი', 'G-Force ევრო რეგულარი', 'ევრო რეგულარი',
                  'G-Force ევრო დიზელი', 'ევრო დიზელი', 'გაზი'])

while payload['page'] < 6:
    response = requests.get(url, params=payload, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    petrol_soup = soup.find('div', class_='price_entries_inner')
    all_petrol = petrol_soup.find_all('tr', class_='prices_cnt')

    for petrol in all_petrol:
        year = petrol.td.span.text.strip()
        GS = petrol.find_all('td')[1].span.text.strip()
        GP = petrol.find_all('td')[2].span.text.strip()
        GER = petrol.find_all('td')[3].span.text.strip()
        ER = petrol.find_all('td')[4].span.text.strip()
        GED = petrol.find_all('td')[5].span.text.strip()
        ED = petrol.find_all('td')[6].span.text.strip()
        CNG = petrol.find_all('td')[7].span.text.strip()

        try:
            GS = float(GS)
            GP = float(GP)
            GER = float(GER)
            ER = float(ER)
            GED = float(GED)
            ED = float(ED)
            CNG = float(CNG)
        except ValueError:
            continue

        data = (year, GS, GP, GER, ER, GED, ED, CNG)
        cur.execute(
            "INSERT INTO Petrol (Date, G_Force_Super, G_Force_Premium, G_Force_Euro_Regular, Euro_Regular, G_Force_Euro_Diesel, Euro_Diesel, Fuel_Gas) VALUES (?,?,?,?,?,?,?,?)",
            data)

        csv_obj.writerow([year, GS, GP, GER, ER, GED, ED, CNG])

    payload['page'] += 1
    time.sleep(random.randint(15, 20))

file.close()
conn.commit()
conn.close()
