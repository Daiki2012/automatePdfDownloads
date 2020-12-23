import os, ssl


def urllibDec():
    print('enabling urllib commands')
    # execute the urllib commands in Mac OS, I had to add these:
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context



def createDir(dirName):
    print('before create dir')

    # create a directory for saving tmporary pdf files
    outputDir = os.getcwd() + '/' + dirName + '/'
    try:
        os.mkdir(outputDir)
    except OSError:
        print ("Creation of the directory %s failed" % outputDir)
    else:
        print ("Successfully created the directory %s " % outputDir)
    return outputDir

