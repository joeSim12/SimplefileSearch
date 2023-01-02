import os
from docx import *


def readingword(docpath, stringlooked):
    document = opendocx(docpath)
    # returns true if found
    if search(document, stringlooked):
        print(" the following file may be about :", stringlooked, "\n", docpath)


path_of_the_folder = r" your folder path"
reqStr = " topic"  # enter the string / topic you want to search in word documents
print("Files in a specified path:")
for filename in os.listdir(path_of_the_folder):  # folder path
    f = os.path.join(path_of_the_folder, filename)  # file
    if os.path.isfile(f) and f.endswith(".doc") or os.path.isfile(f) and f.endswith(".docx"):
        print(readingword(docpath=f, stringlooked=reqStr))

        
        
