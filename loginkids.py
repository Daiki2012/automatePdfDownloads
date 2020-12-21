#python3.8 -m loginkids.py kajik27338@septicvernon.com
# if the page contains a list of pdfs with a simple file names with an incremented number at the end
from __future__ import print_function
import argparse
import mechanicalsoup
from getpass import getpass
from string import ascii_lowercase
import urllib.request

parser = argparse.ArgumentParser(description="Login to allkidsnetwork.")
parser.add_argument("username")
args = parser.parse_args()

args.password = getpass("Please enter your allkidsnetwork password: ")

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

print('before browser open')
browser.open("https://www.allkidsnetwork.com")
browser.follow_link("/account/login")
browser.select_form('.row form')
browser["Email"] = args.username
browser["Password"] = args.password
resp = browser.submit_selected()


# get files with alphabets
target_url_dir = 'https://www.allkidsnetwork.com/writing/trace-the-words/worksheets/'
download_url_dir = '/Users/daikiharaguchi/Documents/mDocuments/kids/trace-letter-words/'
myint = 0
for c in ascii_lowercase:
    file_name = 'trace-letter-'+ c +'-words.pdf'
    target_url = target_url_dir + file_name
    myint = myint + 1
    download_url = download_url_dir + "trace-letter-" + str(myint) + '.pdf'
    #urllib.request.urlretrieve(target_url, download_url)
    response = browser.open(target_url)
    with open(download_url, 'wb') as f:
        f.write(response.content)
