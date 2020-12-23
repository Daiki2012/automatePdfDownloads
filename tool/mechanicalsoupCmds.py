import mechanicalsoup

# setup mechanicalsoup - login to the site
def login(turl, link, form, email, pas):
    print('logining into ' + turl)
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info',
    )
    browser.open(turl)
    browser.follow_link(link)
    browser.select_form(form)
    browser["Email"] = email
    browser["Password"] = pas
    resp = browser.submit_selected()
    return browser;




def downloadFile(targetUrl, downloadUrl, browser):
    try:
        response = browser.open(targetUrl)
        with open(downloadUrl, 'wb') as f:
            f.write(response.content)
    except:
        print('FAIL downloading: ' + targetUrl)
