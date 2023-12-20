import sys
from network import DetectNetwork
from goprofile import ProfileGL
from metamask import Metamask
from twitter import Twitter

class Menu():
    def __init__(self) -> None:
        self.choices = {
            "1" : self.openInOrder,
            "2" : self.openAsDirected,
            "3" : self.openAuto
        }

        self.urls = [
        ]

    def show_menu(self):
        print('''
            1. Open in order
            2. Open as directed
            3. Open automatically
            '''
        )

    def run(self):
        id = 1
        gologin = None
        net = DetectNetwork()

        while True:
            self.show_menu()
            opt = input("Enter an option: ")
            action = self.choices.get(opt)
            if action:
                while id <= 100:
                    id, gologin = action(id, gologin, net)
                    gologin.openTabs(gologin.driver, self.urls)
                    #do task



                    if opt != "3": break
            else: exit(0)

    def openInOrder(self, id, gologin, net):
        if gologin is not None:
            gologin = gologin.closeGL()
        net.changeIP()
        #them dau phay sau duong dan extension neu muon load nhieu extension
        #vd --load-extension=D:\MMO\gologin\extensions\grass,D:\MMO\gologin\extensions\metamask
        gologin = ProfileGL('--load-extension=D:\MMO\gologin\extensions\grass'
        )
        if not gologin.openGL(profile_id=id):
            print("Fail to open Gologin")
            exit(-1)
        id += 1
        return id, gologin

    def openAsDirected(self, id, gologin, net):
        direct = int(input("Input profile number: "))
        id = direct
        return self.openInOrder(id, gologin, net)
    
    def openAuto(self, id, gologin, net):
        return self.openInOrder(id, gologin, net)
