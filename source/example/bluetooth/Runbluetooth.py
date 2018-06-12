from bluetooth import *

service = DiscoveryService()
devices = service.discover(2)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))