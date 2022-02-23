# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import regex as re
import sys
sys.path.insert(1, "/Users/giortt/Desktop/readlang_to_anki/")
from readlang_intgration.parsing import separateFields
from unidecode import unidecode


def generatePlurals():
    file_ptr = open("most frequent nouns", "r")
    ans = open("most_frequent_nouns_with_plurals.txt", "w")

    cards = file_ptr.readlines()
    for card in cards[2:10]:
        new_card = insertPluralInCard(card)
        ans.write(new_card)
        ans.write("\n")

    ans.close()
    file_ptr.close()


def getPluralsFromWebRequest(word):
    ctx = ssl.create_default_context()
    basic_url = "https://www.verbformen.pt/declinacao/substantivos/?w="
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = basic_url+word
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(class_="vStm rCntr")
    for tag in tags:
        plural=tag.get_text().split("\n")[-1]
        plural=parsing(plural)
        #if("/" in plural):
        #    plural = plural.split("/")[1]
        print(plural)

        return plural


def insertPluralInCard( card ):
    word, secondField, thirdField, _ = separateFields(card)
    plural = getPluralsFromWebRequest(word)
    new_card = word+"; "+secondField+", die "+plural+"; "+thirdField

    return new_card


def parsing( text ):
    #chars_with_trema = ["ä","ë","ü","ö","Ü","Ö","Ë"]
    #return re.sub("[^\w|ä|ë|ü|ö|Ü|Ö|Ë|\/]", "", text)

    return re.sub("[^\p{L}|\/]", "", text)


generatePlurals()

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