# move this python file and the pdf files under same folder
from PyPDF2 import PdfFileMerger
import os
from os import listdir
from os.path import isfile, join

outputDir = os.getcwd() + '/tmp/'
os.chdir(outputDir)
print(os.getcwd())

# list all files in the tmp directory except hidden files and output file
pdfs = [f for f in listdir(outputDir) if not f.startswith('.') and not f.startswith('output') and isfile(join(outputDir, f))]
print(pdfs)

merger = PdfFileMerger()
for pdf in pdfs:
    print(pdf)
    merger.append(pdf)
merger.write("output.pdf")
merger.close()


