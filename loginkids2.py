#python3.8 -m loginkids2.py kajik27338@septicvernon.com
from __future__ import print_function
import argparse
import mechanicalsoup
from bs4 import BeautifulSoup
from getpass import getpass
from string import ascii_lowercase
import urllib.request
from urllib.request import urlopen

# execute the urllib commands in Mac OS, I had to add these:
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


parser = argparse.ArgumentParser(description="Login to allkidsnetwork.")
parser.add_argument("username")
args = parser.parse_args()
args.password = getpass("Please enter your allkidsnetwork password: ")

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

# login to the site
browser.open("https://www.allkidsnetwork.com")
browser.follow_link("/account/login")
browser.select_form('.row form')
browser["Email"] = args.username
browser["Password"] = args.password
resp = browser.submit_selected()


# go to the page with donwnloadable links
html = urlopen("https://www.allkidsnetwork.com/writing/sentences/sentence-building-worksheets")
bsObj = BeautifulSoup(html,"html.parser")
result = bsObj.findAll("div", {"class": "masonry-grid-item"})
#print(result)

# get files with scraped downloadable filenames
target_url_dir = 'https://www.allkidsnetwork.com/writing/sentences/worksheets/'
download_url_dir = '/Users/daikiharaguchi/Documents/mDocuments/kids/sentences-worksheets/'
myint = 0
items=bsObj.select('a[data-akn-t="SectionChild|Thumbnail"]')
for item in items:
    file_name = item['href'].rsplit('/', 1)[-1] + '.pdf'
    target_url = target_url_dir + file_name
    myint = myint + 1
    download_url = download_url_dir + "sentence-worksheet" + str(myint) + '.pdf'
    response = browser.open(target_url)
    with open(download_url, 'wb') as f:
        f.write(response.content)



