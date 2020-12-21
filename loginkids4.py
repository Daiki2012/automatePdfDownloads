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

# setup mechanicalsoup - login to the site
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
browser.open("https://www.allkidsnetwork.com")
browser.follow_link("/account/login")
browser.select_form('.row form')
browser["Email"] = 'kajik27338@septicvernon.com'
browser["Password"] = '7@K6rm4ZhZxWsB#'
resp = browser.submit_selected()

print('before urlopen')
# go to the page with multiple donwnload links
homeUrl = "https://www.allkidsnetwork.com"
mainUrl = homeUrl + "/reading/riddles/"
html = urlopen(mainUrl)
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"class": "masonry-grid-item"})
#print(result)

# get files with scraped downloadable filenames
targetUrlDir = mainUrl + 'worksheets/'
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
items=bsObj.select('a[data-akn-t="SectionChild|Thumbnail"]')
for item in items:
    turl = item['href']
    #target_file = item['href'].rsplit('/', 1)[-1]
    target_file = turl.rsplit('/', 1)[-1]
    print("targetfile:" + target_file)

    # if the file name ends with asp, like 'picture-clues2.asp', handle differently
    # ex: https://www.allkidsnetwork.com/reading/riddles/worksheets/picture-clues2.pdf
    if(target_file.find('.asp') > -1):
        print('inside asp')
        modified_name = target_file.replace('.asp','')
        # check if the last string contains number
        if(modified_name[-1].isdigit()):
            modified_name += '.pdf'
        else:
            modified_name += '1.pdf'
        target_url = targetUrlDir + modified_name
    else:
        # ex: https://www.allkidsnetwork.com/worksheets/animals/animal-groups/what-animal-is-it-bee-worksheet.pdf
        target_url = homeUrl + turl + '.pdf'

    myint += 1
    download_url = outputDir + "tmp" + str(myint) + '.pdf'
    try:
        response = browser.open(target_url)
        with open(download_url, 'wb') as f:
            f.write(response.content)
    except:
        print('FAIL downloading: ' + target_url)


