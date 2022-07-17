# https://www.alphavantage.co/physical_currency_list/
#Simple Currency Converted by the use of API for
# API have been used to have live exchange rates

import cmd
import requests

api_key = '!!!!!!!!!!!!!!!!' # Please use your own api key
#Register to the website on top of the code. Thanks!

from_currency = 'GBP'
to_currency = 'EUR'

#Using API from the alphavantage
base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_currency + '&to_currency=' + to_currency +'&apikey='+ api_key

response = requests.get(main_url)
result = response.json()

amount = 50

key = result ['Realtime Currency Exchange Rate']
rate = key ['5. Exchange Rate']

print ('Realtime exchange rate : ')
print (f'1 {from_currency} = {rate} {to_currency}')

print (" ----------------------------------")

print('Converted amount : ')
print (f'{amount} {from_currency} = {float(rate)*amount} {to_currency} ')
# rate have been converted into float as rate is a string value
