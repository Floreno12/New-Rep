import requests
from bs4 import BeautifulSoup

url = 'https://www.binance.com/uk-UA/nft/home?utm_source=binance-header&utm_medium=header'
req = requests.get(url)
par = BeautifulSoup(req.text,'html.parser')
parsing = par.find_all('div',class_='css-1rwh7zc')
for giv in parsing:
 print(giv.text)
class Enim:
  parsin = par.find_all('div',class_='css-dp7amh')
  for las in parsin:
   print(las.text)

