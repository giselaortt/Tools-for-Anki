# -*- coding: latin-1 -*-
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import regex as re
import sys
sys.path.insert(1, "/Users/giortt/Desktop/readlang_to_anki/")
from readlang_intgration.parsing import separateFields
from unidecode import unidecode
import time


def getFirstField(card):

    return separateFields(card)[0]


def generatePlurals():
    file_ptr = open("most frequent nouns", "r")
    ans = open("most_frequent_nouns_with_plurals.txt", "r+")
    last_word = getFirstField( ans.readlines()[-1] )
    current_word = None

    while( current_word != last_word ):
        card = file_ptr.readline()
        current_word = getFirstField( card )

    card = file_ptr.readline()

    while( card != "" ): 
        new_card = insertPluralInCard(card)
        print(new_card)
        ans.write(new_card)
        ans.write("\n")
        card = file_ptr.readline()

    ans.close()
    file_ptr.close()


def getPluralsFromWebRequest( word ):
    if(" " in word ):
        word = word.split(" ")[0]
    ctx = ssl.create_default_context()
    basic_url = "https://www.verbformen.pt/declinacao/substantivos/?w="
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = basic_url+unidecode(word)
    time.sleep(10)
    time = 30

    while( True ):
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            break
        except:
            time.sleep(time)
            time = time*2
    
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find(class_="vStm rCntr")
    if( tag is not None ):
        plural=tag.get_text().split("\n")[-1]
        plural=parsing(plural)
        print(plural)
    else:
        plural = None

    return plural


def insertPluralInCard( card ):
    word, secondField, thirdField, _ = separateFields(card)
    plural = getPluralsFromWebRequest(word)
    if( plural is not None ):
        new_card = word+"; "+secondField+", die "+plural+"; "+thirdField+";"
    else:
        new_card = card

    return new_card


def parsing( text ):
    #chars_with_trema = ["ä","ë","ü","ö","Ü","Ö","Ë"]
    #return re.sub("[^\w|ä|ë|ü|ö|Ü|Ö|Ë|\/]", "", text)

    return re.sub("[^\p{L}|\/]", "", text)


generatePlurals()