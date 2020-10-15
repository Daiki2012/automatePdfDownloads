import urllib.request

# execute the urllib commands in Mac OS, I had to add these:
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

target_url_dir = 'https://print-kids.net/print/kokugo/hiragana-rensyuu-tyouon-sokuon/'
download_url_dir = '/Users/daikiharaguchi/Documents/mDocuments/kids/hiragana-tyouon/'
for x in range(1, 12):
    file_name = 'hiragana-tyouon-easy'+ str(x) +'.pdf'
    target_url = target_url_dir + file_name
    print(target_url)
    download_url = download_url_dir + file_name
    print(download_url)
    urllib.request.urlretrieve(target_url, download_url)

