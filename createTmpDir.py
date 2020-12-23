#python3.8 -m loginkids2.py kajik27338@septicvernon.com
import os, ssl



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

