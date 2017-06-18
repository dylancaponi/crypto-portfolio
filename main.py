import json
import requests

# load config file
with open('config.json') as f:
    cfg = json.load(f)

btc_addresses = cfg['btc_addresses']
eth_addresses = cfg['eth_addresses']

btc_api = 'http://btc.blockr.io/api/v1/address/balance/'
eth_api = 'https://api.etherscan.io/api?module=account&action=balance&address='

btc_convert = 10
eth_convert = 10**18


print '>> BTC balances'
for btc_addr in btc_addresses:
	r = requests.get(btc_api + btc_addr[0])
	print r.json()
	# print btc_addr + ': ' + str(r.json()['data']['balance'])

print '---\n>> ETH balances'
for eth_addr in eth_addresses:
	r = requests.get(eth_api + eth_addr[0])
	# r = requests.get(eth_api + eth_addr[0] + '&tag=latest')
	print r.json()
	# print float(r.json()['result'])/eth_convert
	# print eth_addr + ': ' + str(float(r.json()['result'])/eth_convert)