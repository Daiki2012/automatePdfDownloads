from bs4 import BeautifulSoup
from urllib.request import urlopen
from tool.dirCmds import createDir
from tool.dirCmds import urllibDec
from tool.mechanicalsoupCmds import login
from tool.mechanicalsoupCmds import downloadFile 

# to execute urllib commands on Mac, this is needed:
urllibDec();
# create a directory for saving tmporary pdf files
outputDir = createDir('tmp') 

homeUrl = "https://www.allkidsnetwork.com"
#parentPage = homeUrl + "/reading/riddles/"
parentPage = homeUrl + "/spelling/1st-grade/spelling-at-words.asp"
# downloadable file exists under worksheets directory. The download href tag is generated by javascript
# and could not retrieve with beautifulsoup, the headless chrome might be needed. As workaround, I had to guess
# the downloadable link
targetUrlDir = homeUrl + '/spelling/1st-grade/worksheets/'
#https://www.allkidsnetwork.com/spelling/1st-grade/worksheets/spelling-word-find-an%20words.pdf

# setup mechanicalsoup - login to the site
browser = login(homeUrl, "/account/login", '.row form', 'kajik27338@septicvernon.com', '7@K6rm4ZhZxWsB#')

print('before urlopen')
html = urlopen(parentPage)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"class": "masonry-grid-item"})
#print(result)
items=bsObj.select('a[data-akn-t="SectionChild|Thumbnail"]')
#print(items)


myint = 0
for item in items:
    turl = item['href']
    targetFileName = turl.rsplit('/', 1)[-1]
    print("targetfile:" + targetFileName)

    # if the file name ends with asp, like 'picture-clues2.asp', handle differently
    # ex: https://www.allkidsnetwork.com/reading/riddles/worksheets/picture-clues2.pdf
    customFileName = targetFileName
    if(targetFileName.find('.asp') > -1):
        customFileName = targetFileName.replace('.asp','')
        # check if the last string contains number
        #if(customFileName[-1].isdigit()):
        #    customFileName += '.pdf'
        #else:
        #    customFileName += '1.pdf'

    customFileName += '.pdf'
    targetUrl = targetUrlDir + customFileName

    # create a file name with 2 digits number '01.pdf'
    myint += 1
    downloadUrl = outputDir + "{0:0=2d}".format(myint) + '.pdf'
    downloadFile(targetUrl, downloadUrl, browser)
