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
    parser.add_argument("-o","--output", help="Output file", required=False)
    parser.add_argument("-p","--pause", help="Pause between requests")
    parser.add_argument("-r","--range", help="Range, Default 50")
    parser2 = parser.add_mutually_exclusive_group()
    parser2.add_argument("-s","-silent", help="Silent mode",action="store_true")
    # parser2.add_argument("-v", "--verbose", action="store_true", help="Verbose Mode")
    args = parser.parse_args()

    def __init__(self):
        self.domain = self.args.domain
        self.filetype = self.args.filetype
        # self.verbose = self.args.verbose
        self.file = self.args.file
        self.dorks = self.args.dorks
        self.outputfile = self.args.output
        if self.args.pause:
            self.pause = int(self.args.pause)
        else:
            self.pause = False
        if self.args.range:
            self.range = int(self.args.range)
        else:
            self.range = False
        self.silent = self.args.s

    def tostart(self):
        print('''

      　　　　　　　　　　　　　　　＿__
　　　　　　　　　　　　　,.．　'"´´　.　 ｀` ヽ ､
　　　　　　　　　　 ,．'´　　　　　　　　　　　　 ｀ヽ、
　　　　　　　　 ,. '´　／.　　　　　　　　　　　　 ,.◎ヽ､
　　　　　　　 /　　/　　　　　 　 ,　　　 /　　　ヽ｀ヽ、◎
　　　　　　 //　 /　　　　 ,.　　ｲ　　　/　 l　　　｀`‐ '´、
　　　　　　i/i　 .i 　.i　　 ｲ __ /i　 　 /l　 ﾊ 　 i　　　 i .i
　　　　　　l i　 ｨ.　 |-‐/'l´　/ .|　　/｀|`7 ‐i- /　　　 ﾄ i
　　　　 　 !　i .i､. 　i /=,=!='= .| .／ ='='==,'=/i　　　 .i i.i
　　　　　　　 ヽ!|　 .`i　諏訪i　!´.　　!神ﾄﾘ　/　./　 / l,'
　　　　　　　　　|　i.　!　`=='　　　　　`==´ ./　ｲ／/ |
　　　　　　　　　!　.i ヽ`_､""　　'　　　""　/,.ｲ＿./.　 !
.　　　　　　　　 i　　i.　ヽ､　　 i￣￣i　　 ,.ｲ /￣/　　 i
　　　　　　　　 i　　.| .|　　｀ i ､`_‐_´ ｨ_´.　 ,!==/　　　.i

        ''')
        print("""
        Made by \033[1;31mF3rr3ira\033[0;0m :skull:
        GITHUB --> \033[1;31mgithub.com/ferreiraklet\033[0;0m
        \033[1;31mAline\033[0;0m is a tool to download files with google dorks\n""")


    def aline(self):
        url = self.domain
        ext = self.filetype

        if not self.silent:
            self.tostart()
            print("\033[0;34m[*] - \033[0;0mStarting Aline...")
        else:
            print("\033[0;34m[*] - \033[0;0mStarting Aline...")
        try:
            if url.startswith("http"):
                print("\n\033[1;31m[!] -\033[0;0m Specify the website's link without protocol! Exiting...")
                sys.exit()


            # files = os.popen(f"lynx --dump 'https://google.com/search?q=site:{url}+ext:{ext}' | grep '.pdf' | cut -d '=' -f2 | egrep  -v 'site|google' | sed 's/...$//'").readlines()

            files = []
            limit = int(input("\033[1;31m[-] -\033[0;0m Please specify a limit for searching: "))
            if self.pause:
                pause = self.pause
            else:
                pause = 2

            for result in search(f"site:{url} ext:{ext}", lang="en", start=0, stop=limit, pause=pause):
                if result.endswith(f".{ext}"):
                    files.append(result)


            folder = url.replace(".","")

            if not os.path.exists(folder):
                os.popen(f"mkdir {folder}")

            time.sleep(1)
            os.chdir(f"{os.getcwd()}/{folder}")

            cont = 0
            starttime = datetime.datetime.now()
            print(f"\033[95m[+] - \033[0;0m Started Time: {starttime}")

            user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
            "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
            "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
            random.shuffle(user_agents)
            headers = {"User-Agent": user_agents[0]}

            for file in files:

                file = file.replace("\n","")
                cont += 1
                print(f"\033[95m[+]\033[0;0m Downloading --> {file}")

                r = requests.get(file, headers=headers)
                data = r.content
                if r.status_code != 200:
                    print(f"\033[1;31m[!]\033[0;0m Download failed! Code: {r.status_code} -- {file}")
                else:
                    with open(f"{url}{cont}.{ext}", "wb") as l:
                        l.write(data)

            end = datetime.datetime.now()
            print(f"\033[1;31m[-]\033[0;0m Ended Time: {end}")

        except KeyboardInterrupt:
            print("\nExiting... ¯\_(ツ)_/¯ ")
            sys.exit()

        except Exception as ex:
            print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
            sys.exit()


    def alinefile(self):
        print(f"\033[0;34m[*] - \033[0;0mStarting Aline On {self.file}...")
        try:

            if not os.path.exists("logs"):
                os.popen("mkdir logs")

            # files_list = []
            f = open(self.file,"r")
            files_list = f.readlines()
            f.close()


            time.sleep(1)
            os.chdir("logs")

            cont = 0
            starttime = datetime.datetime.now()
            print(f"\033[95m[+]\033[0;0m Started Time: {starttime}")

            user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
            "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
            "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
            random.shuffle(user_agents)
            headers = {"User-Agent": user_agents[0]}
            # withopen

            for pdf in files_list:
                pdf = pdf.replace("\n","")
                cont += 1
                print(f"\033[95m[+]\033[0;0m Downloading [{pdf}]")
                pdfname = pdf.replace("http://","").replace("https://","").replace("/","*")
                # print(pdfname)

                r = requests.get(pdf, headers=headers, allow_redirects=True)
                data = r.content

                if r.status_code != 200:
                    print(f"\033[1;31m[!]\033[0;0m Download failed! Code: {r.status_code} -- {pdf}")
                    # print(r.content)
                    continue
                else:
                    # print(f"{pdfname}{cont}.{pdfname[-3:]}")
                    with open(f"{pdfname}", "wb") as l:
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
        if not self.silent:
            try:
                print(f"\033[0;34m[*] - \033[0;0m Starting Aline...")
                starttime = datetime.datetime.now()
                print(f"\033[95m[+]\033[0;0m Started Time: {starttime}\n")

                if not self.range:
                    limit = 50
                else:
                    limit = self.range
                if self.outputfile:
                    logname = str(self.outputfile)
                else:
                    logname = 0
                #if limit.isdigit() == False:
                    #print("Wrong input! Exiting...")
                    #sys.exit() # verifyexception
                cont = 0
                log_save = []
                if "+" in self.dorks:
                    self.dorks = self.dorks.replace("+"," ")
                if self.pause:
                    pause = self.pause
                else:
                    pause = 2
                for dork in search(self.dorks, tld="com", lang="en", stop=limit, start=0, pause=pause):
                    cont += 1
                    print(f"{cont} \033[95m[+] - \033[0;0m{dork}")
                    log_save.append(dork)

                if logname != 0:
                    try:
                        print("\n\033[95m[+]\033[0;0m Saving log file...")
                        with open(logname, "w") as l:
                            for item in log_save:
                                l.write(f"{item}\n")
                    except:
                        pass

                end = datetime.datetime.now()
                print(f"\033[1;31m[-]\033[0;0m Finished! (ツ) Ended Time: {end}")

            except KeyboardInterrupt:
                print("\nExiting...¯\_(ツ)_/¯")
                sys.exit()
            except FileNotFoundError:
                print("\033[1;31m[!]\033[0;0m No file was specified! No log file was created.")

            except Exception as ex:
                print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
                sys.exit()

        else:
            try:


                if not self.range:
                    limit = 50
                else:
                    limit = self.range

                if self.outputfile:
                    logname = str(self.outputfile)
                else:
                    logname = 0
                #if limit.isdigit() == False:
                    #print("Wrong input! Exiting...")
                    #sys.exit() # verifyexception
                cont = 0
                log_save = []
                if "+" in self.dorks:
                    self.dorks = self.dorks.replace("+"," ")

                user_agents = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
                "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
                random.shuffle(user_agents)
                if self.pause:
                    pause = self.pause
                else:
                    pause = 2
                for dork in search(self.dorks, tld="com", lang="en", stop=limit, start=0, user_agent=user_agents[0],pause=pause):
                    cont += 1
                    # print(dork)
                    log_save.append(dork)

                if logname != 0:
                    try:
                        with open(logname, "w") as l:
                            for item in log_save:
                                l.write(f"{item}\n")
                    except:
                        pass
                print("\033[95m[+]\033[0;0m Finished! (ツ)")

            except KeyboardInterrupt:
                print("\nExiting...¯\_(ツ)_/¯ ")
                sys.exit()
            except FileNotFoundError:
                print("\033[1;31m[!]\033[0;0m No file was specified! No log file was created.")

            except Exception as ex:
                print(f"\033[1;31m[!]\033[0;0m - Something went wrong!\nError: {str(ex)}")
                sys.exit()

    """def ldorks(self):
        # print("Starting...\n")
        self.tostart()

        try:
            log = []
            cont = 0
            dork_range = int(input("\033[1;31m[-]\033[0;0m Please specify a limit, Default = 50: "))
            log_name = str(input("\033[1;31m[-]\033[0;0m Please specify a log file: "))
            dork = str(input("\033[1;31m[-]\033[0;0m Put the dorks here and use 'site:*' for the targets: "))

            with open(self.links,"r") as d:
                for link in d.readlines():
                    link = link.replace("\n","").replace("http://","").replace("https://","")


                    if "*" in dork:
                        dork = dork.replace("*",link)

                    # print(dork)

                    for dorks in search(dork, tld="com", lang="en", num=dork_range, start=0, stop=dork_range, pause=2):
                        cont += 1
                        print(dorks)
                        log.append(dorks)

            with open(log_name,"w") as lg:
                for text in log:
                    lg.write(f"{text}\n")

            print("\033[1;32mFinished! (ツ)\033[0;0m")


        except Exception as e:
            print(f"Something happened!\nError: {str(e)}");exit(1)

        except KeyboardInterrupt:
                print("\nExiting...¯\_(ツ)_/¯ ")
                sys.exit()
        except FileNotFoundError:
            print("\033[1;31m[!]\033[0;0m No file was specified! No log file was created.");exit(1)
                   """

if len(sys.argv) <= 1:
    print("""usage: aline.py [-h] [-d DOMAIN] [-f FILETYPE] [-F FILE] [-D DORKS] [-o OUTPUT] [-r RANGE] [-s] [-v]

Aline file downloader automator!

optional arguments:
  -h, --help            show this help message and exit:
  -d DOMAIN, --domain DOMAIN
                        Target's domain
  -f FILETYPE, --filetype FILETYPE
                        Filetype
  -F FILE, --file FILE  Read a file and download containing links
  -D DORKS, --dorks DORKS
                        Dorks
  -o OUTPUT, --output OUTPUT
                        Output file
  -r RANGE, --range RANGE
                        Range, Default 50
  -s, -silent           Silent mode
  -p PAUSE, --pause PAUSE
                        Pause between Requests""")
    sys.exit()


A = AlineDownloader()

if A.domain and A.filetype:
    A.aline()

elif A.file:
    A.alinefile()

elif A.dorks and not A.silent:
    A.tostart()
    A.dorks_handler()

elif A.dorks and A.silent:
    A.dorks_handler()

elif A.links:
    A.ldorks()

else:
    print("""usage: aline.py [-h] [-d DOMAIN] [-f FILETYPE] [-F FILE] [-D DORKS] [-o OUTPUT] [-r RANGE] [-s] [-v]

Aline file downloader automator!

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target's domain
  -f FILETYPE, --filetype FILETYPE
                        Filetype
  -F FILE, --file FILE  Read a file and download containing links
  -D DORKS, --dorks DORKS
                        Dorks
  -o OUTPUT, --output OUTPUT
                        Output file
  -r RANGE, --range RANGE
                        Range, Default 50
  -s, -silent           Silent mode
  -p PAUSE, --pause PAUSE
                        Pause Between Requests""")


