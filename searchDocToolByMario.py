import os
import PyPDF2
import re
from docx import *


def readingword(docpath, stringlooked):
    document = opendocx(docpath)
    # returns true if found
    if search(document, stringlooked):
        print(" the following word document may be about :", stringlooked, "\n", docpath)


def readPdf(docpath, stringlooked):
    reader = PyPDF2.PdfReader(docpath)
    num_pages = len(reader.pages)
    for page in reader.pages:
        text = page.extract_text()
        # print(text)
        res_search = re.search(stringlooked, text)
        if res_search:
            print("the following pdf document may be about: ",stringlooked, "\n", docpath)


path_of_the_folder = r" your folder path"

reqStr = input("enter word to search:\n")  # enter the string / topic you want to search
while reqStr == "":
    print("invalid input")
    reqStr = input("enter word/number to search:\n")
print("Files in a specified path:")

for filename in os.listdir(path_of_the_folder):  # folder path
    f = os.path.join(path_of_the_folder, filename)  # file
    if os.path.isfile(f) and f.endswith(".doc") or os.path.isfile(f) and f.endswith(".docx"):
        print(readingword(docpath=f, stringlooked=reqStr))

    elif os.path.isfile(f) and f.endswith(".pdf") or os.path.isfile(f) and f.endswith(".pdf"):
        readPdf(docpath=f, stringlooked=reqStr)
