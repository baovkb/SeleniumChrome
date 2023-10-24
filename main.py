import sys, time, os, random, testnet
import twitter, metamask
import pf, network, gleam, mail
import IOFile as file
import Fill as fill

def main():
    url = [
    ]
    
    urlTwTask = [
    ]

    urlFillTask = [
    ]

    dicXpath = {
        'email' : '',
        'usenameTele' : '',
        'linkTele' : '',
        'usernameTw' : '',
        'linkTw' : '',
        'usernameDiscord' : '',
        'usernameDiscordWith#' : '',
        'metamaskAddress' : '',
        'solanaAddress' : '',
        'linkQuoteTw' : ''
    }

    #khoi tao
    opt = 0
    gologin = None
    id = 1
    getInfo = None
    file.init() #file luu lai ket qua
    eDcom = network.isDcom()
    eEtherNet = network.isEthernet()
    
    while id <= 100:
        numTry = 0
        proxyy = ''
        #ip:port:username:pass or ip:port
        #proxyy = network.changeIp('ab43807c-9c85-4837-b5c7-2fade7c8209a') + ':LZprgJ:hBJ1S9'

        os.system('cls')
        print('1. Mo theo thu tu')
        print('2. Mo chi dinh')
        print('3. Lay thong tin profile')
        print('5. Auto')
        
        if opt != 5:
            opt = int(input('Chuc nang: '))
        if opt == 5:
            if eDcom == False and proxyy == '':
                while network.isConnect() == True:
                    print('Ngat ket noi 3g/4g')
                    time.sleep(0.5)
            try:
                gologin = gologin.closeGL()
            except: pass
        if opt == 1 or opt == 2:
            if opt == 2:
                index_input = int(input('Index:'))
            if eEtherNet == True:
                while network.isConnect() == True:
                    print('Ngat ket noi 3g/4g')
                    time.sleep(0.5)
        elif opt == 3:
            getInfo = file.OpenNodeInfo(id - 1)
            continue
        
        if gologin is not None:
            gologin = gologin.closeGL()
        
        if eDcom == True:
            network.changeIpDcom()

        
        while numTry < 3:
            try:
                #dong cac app va profile
                getInfo = file.CloseNodeInfo(getInfo)

                if gologin is not None:
                    gologin = gologin.closeGL()
                print('Dong profile thanh cong')

                gologin = pf.ProfileGL() #create gologin
                if opt == 1:
                    gologin.openGL(id, proxyy)
                    #driver = profile.openProfile(id, proxyy)
                elif opt == 2:
                    gologin.openGL(index_input, proxyy)
                    id = index_input
                elif opt == 5:
                    if (id > 100) : sys.exit()
                    gologin.openGL(id, proxyy)

                else: sys.exit()

                #chay profile va lam task
                gologin.openMultiTab(url)         

                break
            except ValueError:
                numTry = 3
                getInfo = file.CloseNodeInfo(getInfo)
                gologin = gologin.closeGL()
                break
            except:
                numTry += 1

        file.resultRecord(id, numTry)
        id = id + 1
    

if __name__ == '__main__': 
    main()