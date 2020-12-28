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
mainUrl = homeUrl + "/keisan-tasizan.html"
html = urlopen(mainUrl)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("section", {"class": "section mt20"})
print(result)


items=bsObj.select('a[class="cf"]')
for item in items:
    subParentUrl = item['href']
    if(subParentUrl.find('.html') > -1):
        print("subParentUrl:" + subParentUrl)

        shtml = urlopen(subParentUrl)
        sbsObj = BeautifulSoup(shtml,"html.parser")
        result = sbsObj.findAll("div", {"class": "image_column03 border"})
        sItems=sbsObj.select('a')

        prevFileName = ""
        for sItem in sItems:
            surl = sItem['href']
            # only find a file naem ending with pdf
            # ingore a file name with ans-, as this is answer file
            # ignore duplicate file names
            if(surl.find('matome') > -1 and surl.find('.pdf') > -1 and surl.find('ans') == -1 and surl != prevFileName):
                fileName = surl.rsplit('/', 1)[-1]
                print("surl:" + surl)
                targetUrl = homeUrl + "/" + surl
                downloadUrl = outputDir + fileName
                try:
                    urllib.request.urlretrieve(targetUrl, downloadUrl)
                    prevFileName = surl
                except:
                    print('FAIL downloading: ' + targetUrl)


