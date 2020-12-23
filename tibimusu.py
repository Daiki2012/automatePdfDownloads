#python3.8 -m loginkids2.py kajik27338@septicvernon.com
from __future__ import print_function
import argparse
import mechanicalsoup
from bs4 import BeautifulSoup
from getpass import getpass
from string import ascii_lowercase
import urllib.request
from urllib.request import urlopen
import os, ssl
from tool.dirCmds import createDir
from tool.dirCmds import urllibDec



# to execute urllib commands on Mac, this is needed:
urllibDec();
# create a directory for saving tmporary pdf files
outputDir = createDir('tmp') 



print('before urlopen')
# go to the page with multiple donwnload links
homeUrl = "https://happylilac.net"
mainUrl = homeUrl + "/kazu-hikizan10.html"
html = urlopen(mainUrl)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"class": "image_column03 border"})
#print(result)


myint = 0
prevFileName = ""
items=bsObj.select('a')
for item in items:
    turl = item['href']
    # only find a file naem ending with pdf
    # ingore a file name with ans-, as this is answer file
    # ignore duplicate file names
    if(turl.find('.pdf') > -1 and turl.find('ans') == -1 and turl != prevFileName):
        print("turl:" + turl)
        targetUrl = homeUrl + "/" + turl

        myint += 1
        downloadUrl = outputDir + "{0:0=2d}".format(myint) + '.pdf'
        #print("download:" + downloadUrl)
        try:
            urllib.request.urlretrieve(targetUrl, downloadUrl)
            prevFileName = turl
        except:
            print('FAIL downloading: ' + targetUrl)


