
# MLConvert.py
#
# Description: Parses an .epub file and substitutes all MathML itens for images
#
# Usage: sys.argv[0] <input-file> <output-file>


import sys
import zipfile
from bs4 import BeautifulSoup

inputFilename = sys.argv[1] 
outputFilename = sys.argv[2] if len(sys.argv[2]) != 0 else 'out-' + sys.argv[1]
outputFilename += ".zip"

if not zipfile.is_zipfile(inputFilename):
    print("Error: Not zipfile")
    exit(1)

# Copies output from input
inputFile = open(inputFilename,'rb')
outputFile = open(outputFilename if len(outputFilename)!= 0 else 'out-'+inputFilename,'wb')

chunk = 2046
while True:
    data = inputFile.read(chunk)
    if not data:
        break
    outputFile.write(data)


# Opens .epub (actually zip) file
zipFile = zipfile.ZipFile(outputFilename,'r')

filesList = zipfile.namelist()
imageDir = "OPS/images/"

# Get files
contentList = set([i for i in filesList if i[:10] == "OPS/xhtml/"])

for archive in contentList:
    # Open xhtml file
    with zipfile.open(archive) as fil:
        htmlFile = BeautifulSoup(fil)

