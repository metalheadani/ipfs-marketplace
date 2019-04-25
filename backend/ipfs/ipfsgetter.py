import ipfsapi

api = ipfsapi.connect('https://ipfs.infura.io', 5001)

getter = api.get('QmW64knx23uDeFPXx8KFozgUp497pAck76UYVjSHJvrthR')

print(getter)
getter