import ipfsapi
import json
#from fileupload.views import index

api = ipfsapi.connect('https://ipfs.infura.io', 5001)


def setter(file):
	sendfile = api.add(file)
	return sendfile['Hash']


def getter(ipfsaddr):
	getfile = api.get(ipfsaddr)

