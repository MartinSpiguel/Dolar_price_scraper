import requests
from bs4 import BeautifulSoup

url = 'https://dolarhoy.com/?msclkid=495f79f0c9dc11ec861d9c74473fd644'

site = requests.get(url)
file = site.text

soup = BeautifulSoup(file, 'html.parser')
body = soup.body

dolar_blue = {}

for tag in body:
    dolar_types = tag.parent.find_all('a', class_='title')
    buys_sells = tag.parent.find_all('div', class_='label')
    dolar_vals = tag.parent.find_all('div', class_='val')

for type, buy_sell, val in zip(dolar_types, buys_sells, dolar_vals):
    if type.string == 'Dólar blue':
        dolar_blue[buy_sell.string] = val.string

print('Dólar blue')
print('---------------')
for key, value in dolar_blue.items():
    print(key, ': ', value)