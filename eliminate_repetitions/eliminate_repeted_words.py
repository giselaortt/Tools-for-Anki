import os
import re
import sys
sys.path.insert(1, "/Users/giortt/Desktop/readlang_to_anki/")
from parsers_deutsch_nouns.parsing_nouns import *
from readlang_intgration.parsing import removeBold


def cleanPonctuation( mystr ):

    return re.sub('[^\w\s]', '', mystr)


def cleanNumbers( card ):

    return re.sub( '[0-9]', '', card )


def cutWord( mystr ):
    pass


def getWordsFromFirstField( card ):
    card = cleanNumbers(card)
    card = removeBold(card)
    card = cleanCard(card)
    card = cleanPonctuation(card)
    field = separateFieldsWithTab(card)[0]

    return field.split(" ")


def getWordFromCard( card ):

    return separateFieldsWithTab(card)[1]


if __name__ == "__main__":
    #sys.path.append('../../')
    current_vocabulary = open('Deutsch__vocabulary.txt',"r")
    wordlist = open("wordlist.txt","w")
    my_vocabulary = set()
    cards = current_vocabulary.readlines()

    for card in  cards:
        words = getWordsFromFirstField(card)
        for word in  words:
            my_vocabulary.add(word.lower())

    print(len(my_vocabulary))
    for word in my_vocabulary:
        wordlist.write(word)
        wordlist.write("\n")

    new_deck = open("A Frequency Dictionary of German.txt", "r")
    output_deck = open("neu deutsch wortschatz","w")
    neue_worter = 0
    not_added = 0

    for line in  new_deck.readlines():
        if( getWordFromCard( line ) not in  my_vocabulary ):
            output_deck.write(line)
            neue_worter = neue_worter + 1
        else:
            not_added = not_added + 1

    print(neue_worter, not_added)

    # this is how you apply a function to every element in  place
    # list(map(lambda i:func(a, i), range(0, len(a))))

    #and this is not in  place 
    # map(upper, mylis)
