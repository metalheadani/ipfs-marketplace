import ipfsapi

api = ipfsapi.connect('https://ipfs.infura.io', 5001)

res = api.add('/home/mrrobot/model.ckpt-240050.data-00000-of-00001')

print(res)
res