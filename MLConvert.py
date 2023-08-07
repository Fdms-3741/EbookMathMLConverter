
# MLConvert.py
#
# Description: Parses an .epub file and substitutes all MathML itens for images
#
# Usage: sys.argv[0] <input-file> <output-file>


import sys
import zipfile
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup

# Changes the math elements for each file, given as a fd
from ConvertElements import ConvertMathElements



# Define names for files
inputFilename = Path(sys.argv[1]) 
outputFilename = Path(sys.argv[2] if len(sys.argv) > 2 and len(sys.argv[2]) != 0 else 'out-' + sys.argv[1])

# Have to add suffix .zip to properly unzip it (with zipfile)
zippedFilename = inputFilename.parent / (inputFilename.stem + ".zip")

# Moves input file to folder
subprocess.run(['mv',inputFilename, Path.cwd() /  zippedFilename])

# If file is not zip, exits
if not zipfile.is_zipfile(zippedFilename):
    print("ERROR: File is invalid .epub format")
    subprocess.run(['mv',Path.cwd() /  zippedFilename,inputFilename])
    exit(1)




# Opens input and output file
inputFile = zipfile.ZipFile(zippedFilename)
outputFile = zipfile.ZipFile(outputFilename.stem + ".zip",'w')


# CONVERSION STEP
# Reads each element in the zip file
for item in inputFile.namelist():
    # Copies every item to the new zipfile
    with outputFile.open(item,'w') as outputItem:
        if item.find("OPS/xhtml/") != -1 and item.find('.xhtml') != -1: # finds the content files 
            outputItem.writestr(item,ConvertMathElements(inputFile.open(item))) # Converts the math
        else:
            outputItem.writestr(item,inputFile.open(item,'r').read()) # Copies every other file as is

# Closesfiles
inputFile.close()
outputFile.close()


# Removes extra .zip at the end
subprocess.run(['mv',outputFilename.stem+".zip",outputFilename])
subprocess.run(['mv',Path.cwd() /  zippedFilename,inputFilename])


