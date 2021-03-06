from tkinter import *
import requests, threading, json, io, random
from requests_oauthlib import OAuth1
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Application:
    def threadExec(self,func):
        lines = self.getinput()
        print(lines)
        threads = []
        nThreads = int(self.numberofThread.get())
        self.labelStatus.configure(text="Running")
        for cof in range(nThreads):
            t = threading.Thread(target=func, args=[nThreads, cof, lines])
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()
        self.labelStatus.configure(text="Done")

    def setTextInput(self, text):
        self.inputEntry.delete(1.0,"end")
        self.inputEntry.insert(1.0, ''.join(text))

    def getinput(self):
        lines = io.StringIO(self.inputEntry.get("1.0", "end -1 chars")).readlines()
        return lines

    def saveOutput(self, fname="unknown", flines=""):
        f = open(f"{fname}_output.txt", 'w', encoding="utf-8")
        f.writelines(flines)

    def inputtwitterAPI(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            if(iteration%nThr != thr):
                continue
            API = line.split()
            if len(API) < 4:
                inputlines[iteration] = ",,,,\n"
                self.saveOutput("twitterAPIs",inputlines)
                continue
            inputlines[iteration] = f"{API[0]},{API[1]},{API[2]},{API[3]},{self.checktwitterAPI(API[0], API[1], API[2], API[3])}\n"
            self.saveOutput("twitterAPIs",inputlines)
        self.setTextInput(inputlines)

    def checktwitterAPI(self,YOUR_APP_KEY=None,YOUR_APP_SECRET=None,USER_OAUTH_TOKEN=None,USER_OAUTH_TOKEN_SECRET=None,):
        if YOUR_APP_KEY is None:
            return ''
        url = "https://api.twitter.com/1.1/account/verify_credentials.json"
        auth = OAuth1(YOUR_APP_KEY, YOUR_APP_SECRET, USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)
        content = requests.get(url, auth=auth).text
        parsed_json = json.loads(content)
        if('id' in parsed_json):
            return 'Alive'
        elif('errors' in parsed_json):
            return parsed_json

    def inputtwitterImpactAPI(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            if(iteration%nThr != thr):
                continue
            API = line.split()
            if len(API) < 4:
                inputlines[iteration] = ",,,,\n"
                self.saveOutput("twitterAPIs",inputlines)
                continue
            inputlines[iteration] = f"{API[0]},{API[1]},{API[2]},{API[3]},{self.checktwitterImpactAPI(API[0], API[1], API[2], API[3])}\n"
            self.saveOutput("twitterAPIs",inputlines)
        self.setTextInput(inputlines)

    def checktwitterImpactAPI(self,YOUR_APP_KEY=None,YOUR_APP_SECRET=None,USER_OAUTH_TOKEN=None,USER_OAUTH_TOKEN_SECRET=None,):
        if YOUR_APP_KEY is None:
            return ''
        url = "https://api.twitter.com/1.1/statuses/destroy/240854986559455234.json"
        auth = OAuth1(YOUR_APP_KEY, YOUR_APP_SECRET, USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)
        content = requests.post(url, auth=auth).text
        parsed_json = json.loads(content)
        return parsed_json
        # if('id' in parsed_json):
        #     return 'Alive'
        # elif('errors' in parsed_json):
        #     return parsed_json

    def inputyoutubeAPI(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            if(iteration%nThr != thr):
                continue
            API = line.split()
            if len(API) < 1:
                inputlines[iteration] = ",\n"
                self.saveOutput("youtubeAPIs",inputlines)
                continue
            inputlines[iteration] = f"{str(API[0])},{self.checkYoutubeAPI(API[0])}\n"
            print(inputlines[iteration])
            self.saveOutput("youtubeAPIs",inputlines)
        self.setTextInput(inputlines)

    def checkYoutubeAPI(self, API=None):
        if API is None:
            return ''
        content = requests.get(f"https://www.googleapis.com/youtube/v3/commentThreads?key={API}&part=id,replies,snippet&videoId=Rck7CeKBF3U&maxResults=1&order=time&regionCode=VN").text
        parsed_json = json.loads(content)
        if('kind' in parsed_json):
            return 'Alive'
        elif('error' in parsed_json):
            return parsed_json['error']['errors'][0]['reason']

    def inputlinkedinAPI(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            if(iteration%nThr != thr):
                continue
            API = line.split()
            if len(API) < 2:
                inputlines[iteration] = ",,\n"
                self.saveOutput("linkedinAPIs",inputlines)
                continue
            sleep(random.randint(0,60))
            inputlines[iteration] = f"{API[0]},{API[1]},{self.checklinkedinAPI(API[0], API[1])}\n"
            print(inputlines[iteration])
            self.saveOutput("linkedinAPIs",inputlines)
        self.setTextInput(inputlines)

    def checklinkedinAPI(self, liat, Jses):
        headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           }
        company_link = 'https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=williamhgates&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
        try:
            with requests.session() as s:
                s.cookies['li_at'] = liat
                s.cookies["JSESSIONID"] = Jses
                s.headers = headers
                s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
                response = s.get(company_link)
                response_dict = response.json()
                if 'elements' in response_dict:
                    return 'Alive'
                else:
                    return 'NeedCheck'
        except:
            return 'Die'

    def inputvkAPI(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            if(iteration%nThr != thr):
                continue
            API = line.split()
            if len(API) < 1:
                inputlines[iteration] = ",\n"
                self.saveOutput("vkAPIs",inputlines)
                continue
            inputlines[iteration] = f"{str(API[0])},{self.checkvkAPI(API[0])}\n"
            print(inputlines[iteration])
            self.saveOutput("vkAPIs",inputlines)
        self.setTextInput(inputlines)

    def checkvkAPI(self, API=None):
        if API is None:
            return ''
        content = requests.get(f"https://api.vk.com/method/getProfiles?uid=66748&v=5.131&access_token={API}").text
        parsed_json = json.loads(content)
        if('response' in parsed_json):
            return 'Alive'
        elif('error' in parsed_json):
            return 'Error'

    def inputLinkedinAccount(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            print(iteration)
            user = line.split()
            inputlines[iteration] = f"{str(user[0])},{str(user[1])},{self.getLinkedinToken(user[0], user[1])}\n"
            print(inputlines[iteration])
            self.saveOutput("LinkedinToken",inputlines)
            self.setTextInput(inputlines)

    def getLinkedinToken(self, username, password):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=3")
        chrome_options.headless = True
        driver = webdriver.Chrome(executable_path='driver/chromedriver.exe',options=chrome_options,service_log_path='NUL')
        try:
            driver.get("https://www.linkedin.com/")
            driver.find_element_by_id('session_key').send_keys(username)
            driver.find_element_by_id('session_password').send_keys(password, Keys.ENTER)
            sleep(3)
            cookies = driver.get_cookies()
            format = ""
            for i, cookie in enumerate(cookies):
                format += cookie['name'] + "=" + cookie['value']
                if i < len(cookies)-1:
                    format += ";"
            if "li_at=" not in format:
                format = "Exception"
        except:
            format = "Exception"
        driver.quit()
        return format


    def inputAgentId(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            print(iteration)
            user = line.split()
            inputlines[iteration] = f"{str(user[0])},{self.getPath(user[0])}\n"
            print(inputlines[iteration])
            self.saveOutput("Path",inputlines)
            self.setTextInput(inputlines)

    def getPath(self, agentId):
        try:
            r = json.loads(requests.get("http://125.138.183.122:8084/deepsignal-de-tool/api/agent/agentInfo?serverName=DeepSignal&agentId="+agentId).text)['data']['path']
        except Exception as e:
            r = ""
        return r

    def inputLinkedinAccountLiatJses(self, nThr=1, thr=0, inputlines=None):
        for iteration, line in enumerate(inputlines):
            print(iteration)
            user = line.split()
            inputlines[iteration] = f"{str(user[0])},{str(user[1])},{self.getLinkedinTokenLiatJses(user[0], user[1])}\n"
            print(inputlines[iteration])
            self.saveOutput("LinkedinToken",inputlines)
            self.setTextInput(inputlines)

    def getLinkedinTokenLiatJses(self, username, password):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=3")
        chrome_options.headless = True
        driver = webdriver.Chrome(executable_path='driver/chromedriver.exe',options=chrome_options,service_log_path='NUL')
        driver.get("https://www.linkedin.com/")
        driver.find_element_by_id('session_key').send_keys(username)
        driver.find_element_by_id('session_password').send_keys(password, Keys.ENTER)
        sleep(3)
        try:
            liat = driver.get_cookie('li_at')['value']
            jses = driver.get_cookie('JSESSIONID')['value']
        except:
            return ('error');
        driver.quit()
        return f"{liat},{jses}"


    def main_form(self):
        self.root = Tk()
        self.root.minsize(width=300, height=300)
        self.root.title('API Checker')
        self.root.iconbitmap(r"pepe.ico")

        statusFrame = Frame(self.root, relief="flat")
        self.labelStatus = Label(statusFrame, text="Status")
        self.labelStatus.pack()
        statusFrame.pack()

        threadFrame = Frame(self.root, relief="flat")

        self.label1 = Label(threadFrame, text="Choose number of thread to run function:")
        self.label1.pack()
        
        OPTIONS = [1,2,4,8,32,64,128] #etc
        self.numberofThread = StringVar(threadFrame)
        self.numberofThread.set(OPTIONS[0]) # default value

        w = OptionMenu(threadFrame, self.numberofThread, *OPTIONS)
        w.pack()
        threadFrame.pack()
        
        txtFrame = Frame(self.root, borderwidth=1, relief="flat")

        self.ybars = Scrollbar(txtFrame)
        self.ybars.pack(side=RIGHT, fill=Y)
        self.xbars = Scrollbar(txtFrame, orient='horizontal')
        self.inputEntry = Text(txtFrame,height=12, width=50, wrap="none", yscrollcommand=self.ybars.set, xscrollcommand=self.xbars.set)
        self.inputEntry.pack(side=TOP)
        self.xbars.pack(side=TOP, fill=X)
        self.xbars.config(command=self.inputEntry.xview)
        self.ybars.config(command=self.inputEntry.yview)

        txtFrame.pack()

        fncFrame = Frame(self.root, borderwidth=1, relief="flat")

        self.function_1 = Button(fncFrame, text="TwitterAPIs", command=lambda: self.sci_thread('twAPI'))
        self.function_1.pack(side = LEFT, padx=5, pady= 5)

        self.function_1 = Button(fncFrame, text="TwitterImpactAPIs", command=lambda: self.sci_thread('twImpactAPI'))
        self.function_1.pack(side = LEFT, padx=5, pady= 5)

        self.function_2 = Button(fncFrame, text="YoutubeAPIs", command=lambda: self.sci_thread('ytAPI'))
        self.function_2.pack(side = LEFT, padx=5, pady= 5)

        self.function_3 = Button(fncFrame, text="LinkedInAPIs", command=lambda: self.sci_thread('liAPI'))
        self.function_3.pack(side = LEFT, padx=5, pady= 5)

        self.function_4 = Button(fncFrame, text="VKAPIs", command=lambda: self.sci_thread('vkAPI'))
        self.function_4.pack(side = LEFT, padx=5, pady= 5)

        self.function_5 = Button(fncFrame, text="Get token Linkedin", command=lambda: self.sci_thread('execLinkedinToken'))
        self.function_5.pack(side = LEFT, padx=5, pady= 5)

        self.function_6 = Button(fncFrame, text="Get token Linkedin Liat Jses", command=lambda: self.sci_thread('execLinkedinTokenLiatJses'))
        self.function_6.pack(side = LEFT, padx=5, pady= 5)

        self.function_7 = Button(fncFrame, text="Get Path", command=lambda: self.sci_thread('excGetPath'))
        self.function_7.pack(side = LEFT, padx=5, pady= 5)

        self.QUIT = Button(fncFrame,text="QUIT", fg="red", command=self.root.quit)
        self.QUIT.pack(side = RIGHT)

        fncFrame.pack()

        self.root.update()
        self.root.mainloop()

    def sci_thread(self,fncname=""):
        if fncname == 'vkAPI':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputvkAPI])
        elif fncname == 'twAPI':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputtwitterAPI])
        elif fncname == 'twImpactAPI':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputtwitterImpactAPI])
        elif fncname == 'ytAPI':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputyoutubeAPI])
        elif fncname == 'liAPI':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputlinkedinAPI])
        elif fncname == 'execLinkedinToken':
            self.numberofThread.set(1)
            maincal = threading.Thread(target=self.threadExec, args=[self.inputLinkedinAccount])
        elif fncname == 'execLinkedinTokenLiatJses':
            self.numberofThread.set(1)
            maincal = threading.Thread(target=self.threadExec, args=[self.inputLinkedinAccountLiatJses])
        elif fncname == 'excGetPath':
            maincal = threading.Thread(target=self.threadExec, args=[self.inputAgentId])    
        maincal.start()

co = Application()
mainfz = threading.Thread(target=co.main_form)
mainfz.start() 