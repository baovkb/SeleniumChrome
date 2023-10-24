import subprocess, json, shutil

def init():
    try:
        #khoi tao file ghi lai ket qua
        with open('.\\data\\result.txt', 'w') as result:
            result.write('')
    except: 
        print('Khoi tao file loi')
        raise ValueError

def getProxy(indexProfile):
    try:
        proxy = open('.\\data\\proxy.txt', 'r', encoding='utf-8')
        for i in range(0, indexProfile):
            proxyy = proxy.readline()
        proxy.close()
        return proxyy.replace('\n', '')
    except:
        raise Exception

def changeAuthyProxy(indexProfile, username = "", password = ""):
    try:
        path = "D:\\MMO\\Gologin\\" + str(indexProfile) + "\\Default\\Preferences"
        with open(path, mode='r+', encoding='utf-8') as iFile:
            config = json.load(iFile)
            config["gologin"]["proxy"]["password"] = password
            config["gologin"]["proxy"]["username"] = username
            iFile.seek(0, 0)
            json.dump(config, iFile)
            iFile.truncate()
    except: 
        print('Khong the doi proxy')
        input('Nhan phim bat ki de tiep tuc')

def countProfileInfo():
    try:
        with open('.\\data\\info.txt', 'r', encoding='utf-8') as oF:
            config = json.load(oF)
            return len(config)
    except: 
        raise Exception

def getInfoProfile(indexProfile):
    try:
        with open(".\\data\\info.txt", 'r', encoding='utf-8') as fInfo:
            config = json.load(fInfo)
            Info = config[str(indexProfile)]
            Info['linkTelegram'] = 'https://t.me/' + Info['userTelegram'][1:]
            Info['userDiscord@'] = '@' + Info['userDiscord'].split('#')[0]
            Info['linkTwitter'] = 'https://mobile.twitter.com/' + Info['userTwitter'][1:]
        return Info
    except: 
        raise Exception

def outInfo(indexProfile):
    try:
        Info = getInfoProfile(indexProfile)
        with open(".\\data\\outInfo.txt", 'w', encoding = 'utf-8') as outInfo:
            tmp = list(Info.items())
            for first, second in tmp:
                outInfo.write(first + ': ' + second + '\n')
    except: pass


def countTweetText():
    try:
        fInfo = open('.\\data\\rw_text.txt', 'r')
        readFile = fInfo.readline()
        numInfo = 0
        while readFile != '':
            numInfo = numInfo + 1
            readFile = fInfo.readline()
        fInfo.close()
        return numInfo
    except: 
        raise Exception

def getTweetText(index):
    try:
        txt = ''
        fTw = open('.\\data\\rw_text.txt', 'r')
        for i in range(0, index):
            txt = fTw.readline()
        fTw.close()
        return txt
    except: raise Exception

def getPhrase(index):
    try:
        txt = ''
        fTw = open("D:\\MMO\\wallet\\new\\recovery_phrase.txt", 'r')
        for i in range(0, index):
            txt = fTw.readline()
        fTw.close()
        return txt.replace('\n', '')
    except: raise Exception

def getPk(index):
    try:
        txt = ''
        fTw = open("D:\\MMO\\wallet\\privatekey_evm.txt", 'r')
        for i in range(0, index):
            txt = fTw.readline()
        fTw.close()
        return txt.replace('\n', '')
    except: raise Exception

def resultRecord(indexProfile, numTry):
    with open('.\\data\\result.txt', 'a') as result:
        if numTry < 3:
            result.write('Profile ' + str(indexProfile) + ' hoan tat\n')
        else: result.write('Profile ' + str(indexProfile) + ' bi loi\n')

def readAddress(index):
    with open("D:\\MMO\\wallet\\rdx_add.txt", 'r') as re:
        for i in range(0, index):
            result =re.readline()
        result = result.replace('\n', '')
        result = result.replace(' ', '')
    return result

def readFile(path:str, ind):
    with open(path, 'r') as re:
        for i in range(0, ind):
            result =re.readline()
        result = result.replace('\n', '')
        result = result.replace(' ', '')
    return result


def readFeedback(index):
    with open("D:\\MMO\\Others\\feedback.txt", 'r') as re:
        for i in range(0, index):
            result =re.readline()
        result = result.replace('\n', '')
    return result

def OpenNodeInfo(indexProfile):
    outInfo(indexProfile)
    return subprocess.Popen(['notepad.exe', '.\\data\\outInfo.txt'],creationflags=0x00000008)

def CloseNodeInfo(process):
    if process is not None:
        process.terminate()
        return None
