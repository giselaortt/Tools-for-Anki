import re
from difflib import SequenceMatcher
import sys


def separateFieldsWithTab( card ):

    return card.split("\t")


def cleanCard( card ):

    return re.sub( "\[.{12,13}]","",card )


def getWordAndPlural( field ):
    words = field.split(" ")
    return words[1], words[4]


def checkIfWordsAreSimilar( first, second ):
    if( SequenceMatcher( None, first, second ).ratio() > 0.5 ):
        return True
    else:
        return False


def fieldIncludePlural( card ):

    return re.search( " , ", card )


#TODO: bug fix: some words dont have plural
if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    parsed_file = open("parsedNouns.txt", 'w+')
    excluded = open("excluded.txt", "w+")

    for line in input_file.readlines():
        cleanLine = cleanCard(line)
        secondField = separateFieldsWithTab(cleanLine)[1]
        if( fieldIncludePlural( secondField ) ):
            singular, plural = getWordAndPlural( secondField )
            if( checkIfWordsAreSimilar(singular, plural) ):
                parsed_file.write(cleanLine)
            else:
                excluded.write(cleanLine)
        else:
            parsed_file.write(cleanLine)

    parsed_file.close()
    input_file.close()
    excluded.close()