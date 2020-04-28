import urllib.request

print('Beginning file download with urllib2...')

target_url_dir = 'https://print-kids.net/print/kokugo/hiragana-rensyuu/'
download_url_dir = 'C:/Users/DH039307/Downloads/'
for x in range(1, 47):
    file_name = 'hiragana-rensyuu'+ str(x) +'.pdf'
    target_url = target_url_dir + file_name
    print(target_url)
    download_url = download_url_dir + file_name
    print(download_url)
    urllib.request.urlretrieve(target_url, download_url)

