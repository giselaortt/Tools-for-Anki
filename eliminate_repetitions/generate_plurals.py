# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import re
import sys
sys.path.insert(1, "/Users/giortt/Desktop/readlang_to_anki/")
from readlang_intgration.parsing import separateFields
from unidecode import unidecode




def getPluralsFromWebRequest():
    ans = open("answer.txt", "a")
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    basic_url = "https://www.verbformen.pt/declinacao/substantivos/?w="
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    file_ptr = open("most frequent nouns", "r")
    lines = file_ptr.readlines()
    words = []
    for line in lines:
        words.append( separateFields(line)[0] )
    plurals=[]
    for word in words[1:10]:
        url = basic_url+word
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup.find_all(class_="vStm rCntr")
        for tag in tags:
            print(tag.get_text().split("\n")[-1])
            #ans.write(tag.get_text())

        break

    #print(unidecodeplurals)
    #print(unidecode(plurals[0]))
    ans.close()


def cleanNumbers( card ):

    return re.sub('[0-9]', '', card)


def parsing( ):
    fileptr = open("answer.txt", "r")
    lines = fileptr.readlines()
    for line in lines:
        print(cleanNumbers(line))
    fileptr.close()

parsing()

#getPluralsFromWebRequest()
'''
<p class="vStm rCntr">
<b><i></i>Studium<i>s</i></b>
·
<b><i></i>Studi<u>en</u><i></i></b>⁰


<p class="vStm rCntr">
<b><i></i>Kenntnis<i></i></b>
·
<b><i></i>Kenntnis<i>se</i></b>
'''