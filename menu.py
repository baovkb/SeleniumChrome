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
        }

        self.urls = [
        ]

    def show_menu(self):
        print('''
            1. Open in order
            2. Open as directed
            '''
        )

    def run(self):
        id = 1
        listGologin = None
        net = DetectNetwork()
        proxy = False
        num_thread = 3
        id = 101

        while True:
            self.show_menu()
            opt = input("Enter an option: ")
            action = self.choices.get(opt)
            if action:
                if action == self.openAsDirected:
                    id = int(input('index: '))
                #close previous seasions if not using proxy before open new one
                if listGologin is not None and proxy == False:
                    for l in listGologin:
                        l.closeGL()
                #change ip if not using proxy and length of list id is 1
                if proxy == False:
                    net.changeIP()
                while id <= 110:
                    listGologin = action(listId=[i for i in range(id, id + num_thread)], proxy=proxy)
                    #do task
                    id += num_thread

                    if opt != "3": break
            else: exit(0)

    def openAsDirected(self, listId: list, proxy):
        return self.OpenMultiThread(listId=listId, proxy=proxy)


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
    
    def OpenMultiThread(self, listId: list, proxy):
        listThread = []
        
        for i in range(0, len(listId)):
            listThread.append(Gologin_Threading(target=self.drive, args=(listId[i],proxy,)))
            listThread[i].start()
        
        return [th.join() for th in listThread if (th.join() is not None)]
