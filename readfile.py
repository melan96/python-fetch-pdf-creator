#Read data from given .TXT based file

import sys
import os
import pdfkit
import jinja2
import pandas as pd


def main():
    filePath = sys.argv[1]

    #"C:/Users/meland/Desktop/ReleaseMailExtractor/venv/Scripts/sample.txt"

    if not os.path.isfile(filePath):
        print("file path does not exist {} ...".format(filePath))


    fetchedData = []

    with open(filePath) as fp:
        lineCount=0
        for line in fp:
            #print("line {} contents -> {}".format(lineCount,line))
            fetchedData.append(line)
            lineCount += 1

        print(fetchedData[2])


def createTemplate():
    templateLoader = jinja2.FileSystemLoader(searchPath="./")
    tempateEnv = jinja2.Environment(loader=templateLoader)
    TEMPL_FILE="template.txt"

    template = tempateEnv.get_template(TEMPL_FILE)
    outputText=template.render(data01='templdata')

def dataPDF():
    pdfkit.from_file('sample.txt','return.pdf')



main()



