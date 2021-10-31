import os
import sys
import requests
import argparse
import datetime
import random
import time
from googlesearch import search

class AlineDownloader:
    parser = argparse.ArgumentParser(description="Aline file downloader automator!")
    parser.add_argument("-d", "--domain", help="Target's domain")
    parser.add_argument("-f","--filetype", help="Filetype")
    parser.add_argument("-F","--file", help="Read a file and download containing links")
    parser.add_argument("-D","--dorks", help="Dorks")
    parser2 = parser.add_mutually_exclusive_group()
    parser2.add_argument("-v", "--verbose", action="store_true", help="Verbose Mode")
    args = parser.parse_args()

    def __init__(self):
        self.domain = self.args.domain
        self.filetype = self.args.filetype
        self.verbose = self.args.verbose
        self.file = self.args.file
        self.dorks = self.args.dorks

    def tostart(self):
        print('''

                                  ./\."  
                               ./     \."  
                                \.        \."  
                                  \.        \."
                                    \.        \."  
                                      \.        \." 
                                      ./            \."  
                                    ./            ____ \." 
                                  ./                  <   \."  
                                   \-------\             >    \." 
                                    \=====>        ___<        \." 
                                   ./-----/             __________ \."  
                                    \.------\       _____   ___(_)(_\."\   
                                      \=====>          <            ./" 
                                    ./-----/             >        ./" 
                                    \.               ___<       ./" 
                                      \.                     ./" 
                                         \.                ./" 
                                           \.           ./" 
                                            ./          ./" 
                                          ./          ./  Tool Made By -- Ferreira"
                                        ./          ./" 
                                      ./          ./" 
                                    ./          ./" 
                                     \.        ./"  
                                      \.   ./"  
                                        \/"\n 
        ''')
        print("""
        Made by \033[1;31mF3rr3ira\033[0;0m :skull:
        GITHUB --> \033[1;31mgithub.com/ferreiraklet\033[0;0m
        \033[1;31mAlienware\033[0;0m is a tool to download files with google dorks\n""")


    def aline(self):
        url = self.domain
        ext = self.filetype

        print("\033[1;32m[+]\033[0;0m * Starting Aline...")
        try:
            if url.startswith("http"):
                print("\n\033[1;31m[!] -\033[0;0m Specify the website's link without protocol! Exiting...")
                sys.exit()

                
            # files = os.popen(f"lynx --dump 'https://google.com/search?q=site:{url}+ext:{ext}' | grep '.pdf' | cut -d '=' -f2 | egrep  -v 'site|google' | sed 's/...$//'").readlines()

            files = []
            limit = int(input("\033[1;31m[-] -\033[0;0m Please specify a limit for searching: "))
            for result in search(f"site:{url} ext:{ext}", lang="en", start=0, stop=limit, pause=2,num=limit):
                if result.endswith(f".{ext}"):
                    files.append(result)
                

            folder = url.replace(".com","").replace("br","").replace(".gov","").replace(".","")

            if not os.path.exists(folder):
                os.popen(f"mkdir {folder}")

            time.sleep(1)
            os.chdir(f"{os.getcwd()}/{folder}")

            cont = 0
            starttime = datetime.datetime.now()
            print(f"\033[1;32m[+]\033[0;0m Started Time: {starttime}")

            user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
            random.shuffle(user_agents)
            headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent": user_agents[0]}

            for file in files:

                file = file.replace("\n","")
                cont += 1
                if self.verbose:
                    print(f"\033[1;32m[+]\033[0;0m Downloading --> {file}")

                r = requests.get(file, headers=headers)
                data = r.content
                if r.status_code != 200:
                    if self.verbose:
                        print(f"\033[1;31m[!]\033[0;0m Download failed! Code: {r.status_code} -- {file}")
                else:
                    with open(f"{url}{cont}.{ext}", "wb") as l:
                        l.write(data)

            end = datetime.datetime.now()
            print(f"\033[1;31m[-]\033[0;0m Ended Time: {end}")

        except KeyboardInterrupt:
            print("\nExiting...¯\_(ツ)_/¯ ")
            sys.exit()

        except Exception as ex:
            print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
            sys.exit()


    def alinefile(self):
        print(f"\033[1;32m[+]\033[0;0m * Starting Aline On {self.file}...")
        try:
                
            if not os.path.exists("alinescans"):
                os.popen("mkdir alinescans")

            files_list = []
            f = open(self.file,"r")
            files_list.append(f.read())
            f.close()

            time.sleep(1)
            os.chdir("alinescans")

            cont = 0
            starttime = datetime.datetime.now()
            print(f"\033[1;32m[+]\033[0;0m Started Time: {starttime}")

            user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
            random.shuffle(user_agents)
            headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent": user_agents[0]}
            # withopen

            for pdf in files_list:
                cont += 1
                pdf = pdf.replace("\n","")
                if self.verbose:
                    print(f"\033[1;32m[+]\033[0;0m Downloading --> {pdf}")

                pdfname = pdf.replace(".com","").replace("br","").replace(".gov","").replace(".","").replace("http","").replace("https","").replace("://","").replace("/","")

                r = requests.get(pdf, allow_redirects=True, headers=headers)
                data = r.content

                if r.status_code != 200:
                    print(f"\033[1;31m[!]\033[0;0m Download failed! Code: {r.status_code} -- {pdf}")
                else:
                    with open(f"{pdfname[6:]}{cont}.{pdfname[-3:]}", "wb") as l:
                        l.write(data)

            end = datetime.datetime.now()
            print(f"\033[1;31m[-]\033[0;0m Ended Time: {end}")

        except KeyboardInterrupt:
            print("\nExiting...¯\_(ツ)_/¯ ")
            sys.exit()

        except Exception as ex:
            print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
            sys.exit()



    def dorks_handler(self):
        print(f"\033[1;32m[+]\033[0;0m * Starting Aline On {self.file}...\n")
        try:

            starttime = datetime.datetime.now()
            print(f"\033[1;32m[+]\033[0;0m Started Time: {starttime}")

            limit = int(input("\033[1;31m[-]\033[0;0m Please specify a range for the dorks: "))
            logname = str(input("\033[1;31m[-]\033[0;0m Please specify a name for the log file: "))
            print("\n")
            #if limit.isdigit() == False:
                #print("Wrong input! Exiting...")
                #sys.exit() # verifyexception
            cont = 0 
            log_save = []
            for dork in search(self.dorks, tld="com", lang="en", num=limit, start=0, stop=limit, pause=2):
                cont += 1
                print(f"\033[1;32m[+]\033[0;0m * {dork}")
                log_save.append(dork)

            print("\033[1;32m[+]\033[0;0m --> Saving log file...")
            with open(logname, "w") as l:
                for item in log_save:
                    l.write(f"{item}\n")

            
            end = datetime.datetime.now()
            print(f"\033[1;31m[-]\033[0;0m Ended Time: {end}")

        except KeyboardInterrupt:
            print("\nExiting...¯\_(ツ)_/¯ ")
            sys.exit()

        except Exception as ex:
            print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
            sys.exit()

if len(sys.argv) <= 1:
    print("""usage: aline.py [-h] [-d DOMAIN] [-f FILETYPE] [-F FILE] [-D DORKS] [-v]

Aline file downloader automator!

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target's domain
  -f FILETYPE, --filetype FILETYPE
                        Filetype
  -F FILE, --file FILE  Read a file and download containing links
  -D DORKS, --dorks DORKS
                        Dorks
  -v, --verbose         Verbose Mode""")
    sys.exit()

#if os.getuid() != 0:
    #print("\033[1;31m[!]\033[0;0m --> Need to run as root! Exiting... ¯\_(ツ)_/¯")
    #sys.exit()

A = AlineDownloader()
A.tostart()

if A.domain and A.filetype:
    A.aline()

elif A.file:
    A.alinefile()

elif A.dorks:
    A.dorks_handler()

else:
    print("""usage: aline.py [-h] [-d DOMAIN] [-f FILETYPE] [-F FILE] [-D DORKS] [-v]

Aline file downloader automator!

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target's domain
  -f FILETYPE, --filetype FILETYPE
                        Filetype
  -F FILE, --file FILE  Read a file and download containing links
  -D DORKS, --dorks DORKS
                        Dorks
  -v, --verbose         Verbose Mode""")


