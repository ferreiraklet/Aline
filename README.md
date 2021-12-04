<h1 align="center">Aline</h1> <br>

<p align="center">
  <a href="#--usage">Usage</a> •
  <a href="#--installation--requirements">Installation</a>
</p>

<h3 align="center">Aline's main purpose is to make <a href="https://en.wikipedia.org/wiki/Google_hacking">Google Dorks</a> while, at the same time, be able to download the data recieved from those determined searches.</h3>

<img src="https://cdn.discordapp.com/attachments/307281507431481344/904444564377591889/unknown.png">

## - Installation & Requirements:
```
> git clone https://github.com/ferreiraklet/aline.git

> cd Aline/

> pip3 install -r requirements.txt
```
<br>


## - Usage:

**To Download contents with dorks**:
<img src="https://cdn.discordapp.com/attachments/307281507431481344/904425600809304155/unknown.png">

**Reading files and downloading content within links inside**:

<img src="https://media.discordapp.net/attachments/876919540682989609/916795904944660510/unknown.png?width=472&height=63">

**Dorking**:
```markdown
Usage: python3 aline.py -D "site:.com ext:txt" -o outputfile.txt -r 20 -s

Help pannel:
  -h, --help            :: Show this help message and exit
  
  -d DOMAIN, --domain DOMAIN
                        :: Target's domain

  -f FILETYPE, --filetype FILETYPE
                        :: Filetype

  -F FILE, --file FILE  
                        :: Read a file and download containing links

  -D DORKS, --dorks DORKS
                        :: Dorks

  -o OUTPUT, --output OUTPUT
                        :: Output file

  -r RANGE, --range RANGE
                        :: Range, Default 50
  -s, -silent           :: Silent mode
```
<br>



## This project is for educational porposes only! I do not support any illegal activities!.

If any error in the program, talk to me immediatly. This tool is supposed to work in linux as well as in windows.
