from gologin_threading import Gologin_Threading
from network import DetectNetwork
from goprofile import ProfileGL
from metamask import Metamask
from twitter import Twitter
from IOFile import IOfile

class Menu():
    def __init__(self) -> None:
        self.choices = {
            "1" : self.OpenMultiThread,
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
        listGologin = None
        net = DetectNetwork()
        proxy = False
        listId = [8]

        while True:
            self.show_menu()
            opt = input("Enter an option: ")
            action = self.choices.get(opt)
            if action:
                #close previous seasions if not using proxy before open new one
                if listGologin is not None and proxy == False:
                    for l in listGologin:
                        l.closeGL()
                #change ip if not using proxy and length of list id is 1
                if len(listId) == 1 and proxy == False:
                    net.changeIP()
                while id <= 100:
                    listGologin = action(listId=listId, proxy=proxy)
                    #do task


                    if opt != "3": break
            else: exit(0)

    def drive(self, id, proxy:bool):
        #them dau phay sau duong dan extension neu muon load nhieu extension
        #vd --load-extension=D:\MMO\gologin\extensions\grass,D:\MMO\gologin\extensions\metamask
        gologin = ProfileGL('--load-extension=D:\MMO\gologin\extensions\grass'
        )
        proxyy = ''
        if proxy == True:
            proxyy = IOfile.readFile(path='D:\Downloads\proxy.txt', line=id)
        if not gologin.openGL(profile_id=id, proxy=proxyy):
            print("Fail to open Gologin")
            return None
        
        #do something in here

        return gologin

    def openAsDirected(self, id, gologin, net):
        direct = int(input("Input profile number: "))
        id = direct
        return self.openInOrder(id, gologin, net)
    
    def openAuto(self, id, gologin, net):
        return self.openInOrder(id, gologin, net)
    
    def OpenMultiThread(self, listId: list, proxy):
        listThread = []
        
        for i in range(0, len(listId)):
            listThread.append(Gologin_Threading(target=self.drive, args=(listId[i],proxy,)))
            listThread[i].start()
        
        return [th.join() for th in listThread if (th.join() is not None)]
