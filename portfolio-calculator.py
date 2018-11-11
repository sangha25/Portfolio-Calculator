import requests
from prettytable import PrettyTable

file = open('Portfolio.txt','r')

Symbols = []
Quantitys = []
Buy_prices = []

for line in file.readlines()[1:]:
    line = line.split(',')
    Symbols.append(line[0])
    Quantitys.append(float(line[1]))
    Buy_prices.append(float(line[2]))

api = 'https://api.coinmarketcap.com/v2/listings/'
data = requests.get(api).json()['data']

symbols_id = [0] * len(Symbols)
