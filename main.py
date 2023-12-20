from menu import Menu
from network import *


if __name__ == '__main__': 
    net = DetectNetwork()
    if isinstance(net, Wifi):
        print("using wifi")
    elif isinstance(net, Cellular):
        print("using Cellular")


    #Menu().run()