import sys
from network import Cellular
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
        dcom = Cellular()

        while True:
            self.show_menu()
            opt = input("Enter an option: ")
            action = self.choices.get(opt)
            if action:
                while id <= 100:
                    id, gologin = action(id, gologin, dcom)
                    gologin.openTabs(gologin.driver, self.urls)
                    #do task



                    if opt != "3": break
            else: exit(0)

    def openInOrder(self, id, gologin, dcom):
        if gologin is not None:
            gologin = gologin.closeGL()
        dcom.changeIP()
        #them dau phay sau duong dan extension neu muon load nhieu extension
        #vd --load-extension=D:\MMO\gologin\extensions\grass,D:\MMO\gologin\extensions\metamask
        gologin = ProfileGL('--load-extension=D:\MMO\gologin\extensions\grass'
        )
        if not gologin.openGL(id):
            print("Fail to open Gologin")
            exit(-1)
        id += 1
        return id, gologin

    def openAsDirected(self, id, gologin, dcom):
        direct = int(input("Input profile number: "))
        id = direct
        return self.openInOrder(id, gologin, dcom)
    
    def openAuto(self, id, gologin, dcom):
        return self.openInOrder(id, gologin, dcom)
