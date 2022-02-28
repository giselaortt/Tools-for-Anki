# -*- coding: utf-8 -*-
import os
import re
import sys
sys.path.insert(1, "/Users/giortt/Desktop/readlang_to_anki/")
from parsers_deutsch_nouns.parsing_nouns import *
import parsers_deutsch_nouns.parsing_nouns
from readlang_intgration.parsing import removeBold
from googletrans import Translator
from difflib import SequenceMatcher
from nltk.stem.snowball import GermanStemmer
stemmer = GermanStemmer()
stemmer._GermanStemmer__step1_suffixes = ("innen", "in") + stemmer._GermanStemmer__step1_suffixes


def isCognato( word ):
    translator = Translator()
    english = translator.translate(word, src='de', dest='en').text
    if(SequenceMatcher( None, english, word ).ratio() > 0.9):
        return True
    else:
        return False


def cleanPonctuation( mystr ):

    return re.sub('[^\w\s]', '', mystr)


def cleanNumbers( card ):

    return re.sub('[0-9]', '', card)


def getFirstField( card ):
    field = separateFieldsWithTab(card)[0]

    return field


def eliminateReflexivePronom( word ):

    return re.sub("\(sich\)", "", word)


def eliminateLegend( word ):

    return re.sub( "\(.*\)", "", word )


def getSuffxes( word ):
    if( "(er, e, es)" in word ):
        answer = ["er", "e", "es"]
    if( "(r, s)" in word ):
        answer = ["r", "s"]
    if( "-e, -er, -es" in word ):
        answer = ["e","er","es"]
    else:
        answer = None

    return answer


def eliminateSufixes( wordField ):
    wordField = re.sub("-e, -er, -es", "", wordField)
    wordField.strip(" ")

    return wordField


def glueSuffixes( word, sufixes ):
    ans = [word]
    for sufix in sufixes:
        ans.append(word+sufix)

    return ans


def getWordsFromFirstField( firstField ):
    words = field.lower().split(" ")

    return words


def separateWords( field ):
    field = re.sub(" ","", field)

    return field.split(",")    


def cleanCard( card ):
    card = cleanNumbers(card)
    card = removeBold(card)
    card = parsers_deutsch_nouns.parsing_nouns.cleanCard(card)
    card = cleanPonctuation(card)

    return card
  

def getWordField( card ):

    return separateFieldsWithTab(card)[1]


#todo: Refactor: should receive only the second field, and another function should get the field
def parseFrequentDictionarySecondFild( card ):
    card = card.lower()
    wordField = getWordField( card )
    wordField = eliminateReflexivePronom( wordField )
    wordField = eliminateSufixes( wordField )
    sufixes = getSuffxes( wordField )
    wordField = eliminateLegend( wordField )
    wordField = cleanExtraSpaces( wordField )
    if( sufixes is not None ):
        words = glueSuffixes( wordField, sufixes )
    elif( "," in wordField ):
        words = separateWords( wordField )[0]
    else:
        words = wordField
    #wordField = applyStemmer(wordField)

    return words


def applyStemmer( word):
    
    return stemmer.stem(word)


def createVocabularySet( current_vocabulary ):
    my_vocabulary = set()
    for card in current_vocabulary.readlines():
        card = cleanCard(card)
        field = getFirstField(card)
        words = getWordsFromFirstField(field)
        for word in words:
            #my_vocabulary.add(applyStemmer(word.lower()))
            my_vocabulary.add(word.lower())

    return my_vocabulary


def printSetInFile( my_vocabulary, wordlist ):
    for word in my_vocabulary:
        wordlist.write(word)
        wordlist.write("\n")


def createNewDeck( new_deck, my_vocabulary, output_deck ):
    for line in  new_deck.readlines():
        words = parseFrequentDictionarySecondFild( line )
        if( not bool(my_vocabulary.intersection(set(words))) ):
            output_deck.write(line)


def getFieldFromCard( card, number ):

    return separateFieldsWithTab(card)[number]


def isNounCard( card ):
    artikel = ["der","die","das"]
    if( getFieldFromCard( card, 2 ) in artikel ):
        return True
    return False


def separateNounsFromFrequencyDictionary( new_deck, output_file ):
    for card in new_deck.readlines():
        if(isNounCard(card)):
            output_file.write(getFieldFromCard(card,1))
            output_file.write(";")
            output_file.write(getFieldFromCard(card,2))
            output_file.write(" ")
            output_file.write(getFieldFromCard(card,1))
            output_file.write(";")
            output_file.write(getFieldFromCard(card,3))
            output_file.write(";")
            output_file.write("\n")


if __name__ == "__main__":
    #sys.path.append('../../')
    current_vocabulary = open('Deutsch__vocabulary.txt',"r")
    wordlist = open("wordlist.txt","w")
    new_deck = open("A Frequency Dictionary of German.txt", "r")
    output_deck = open("neu deutsch wortschatz.txt","w")
    most_frequent_nouns = open("most frequent nouns", "w")

    #my_vocabulary = createVocabularySet( current_vocabulary )
    #printSetInFile( my_vocabulary, wordlist )
    #createNewDeck( new_deck, my_vocabulary, output_deck )

    separateNounsFromFrequencyDictionary( new_deck, most_frequent_nouns )

    current_vocabulary.close()
    most_frequent_nouns.close()
    wordlist.close()
    new_deck.close()
    output_deck.close()
    # this is how you apply a function to every element in  place
    # list(map(lambda i:func(a, i), range(0, len(a))))

    #and this is not in  place 
    # map(upper, mylis)
