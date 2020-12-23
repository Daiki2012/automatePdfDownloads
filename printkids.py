from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from tool.dirCmds import createDir
from tool.urllibCmds import urllibDec


# to execute urllib commands on Mac, this is needed:
urllibDec();

print('before urlopen')
# go to the page with multiple donwnload links
homeUrl = "https://print-kids.net/print/sansuu/3tsu-no-tashizan/"
#https://print-kids.net/print/sansuu/3tsu-no-tashizan/3tsu-no-tashizan-keisan1.pdf
html = urlopen(homeUrl)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"id": "topic"})
print(result)

# create a directory for saving tmporary pdf files
outputDir = createDir('tmp') 

myint = 0
prevFileName = ""
items=bsObj.select('a')
for item in items:
    turl = item['href']
    # only find a file naem ending with pdf
    # ignore duplicate file names
    if(turl.find('.pdf') > -1 and turl != prevFileName):
        print("turl:" + turl)
        target_url = homeUrl + "/" + turl

        myint += 1
        # create a file with 2 digits number '01.pdf'
        download_url = outputDir + "{0:0=2d}".format(myint) + '.pdf'
        #print("download:" + download_url)
        try:
            urlretrieve(target_url, download_url)
            prevFileName = turl
        except:
            print('FAIL downloading: ' + target_url)





