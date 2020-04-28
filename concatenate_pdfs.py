# move this python file and the pdf files under same folder
from PyPDF2 import PdfFileMerger

pdfs = []
for x in range(1, 47):
    pdfs.append('hiragana-rensyuu' + str(x) + '.pdf')

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
