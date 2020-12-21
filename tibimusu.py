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


# execute the urllib commands in Mac OS, I had to add these:
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


print('before urlopen')
# go to the page with multiple donwnload links
homeUrl = "https://happylilac.net"
mainUrl = homeUrl + "/kazu-tasizan10.html"
html = urlopen(mainUrl)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"class": "image_column03 border"})
print(result)

#https://www.allkidsnetwork.com/reading/riddles/worksheets/what-animal-is-it-zebra-worksheet.pdf
# create a directory for saving tmporary pdf files
outputDir = os.getcwd() + '/tmp/'
try:
    os.mkdir(outputDir)
except OSError:
    print ("Creation of the directory %s failed" % outputDir)
else:
    print ("Successfully created the directory %s " % outputDir)

myint = 0
prevFileName = ""
items=bsObj.select('a')
for item in items:
    turl = item['href']
    # only find a file naem ending with pdf
    # ingore a file name with ans-, as this is answer file
    # ignore duplicate file names
    if(turl.find('.pdf') > -1 and turl.find('ans-') == -1 and turl != prevFileName):
        print("turl:" + turl)
        target_url = homeUrl + "/" + turl

        myint += 1
        download_url = outputDir + "tmp" + str(myint) + '.pdf'
        #print("download:" + download_url)
        try:
            urllib.request.urlretrieve(target_url, download_url)
            prevFileName = turl
        except:
            print('FAIL downloading: ' + target_url)


