import re
from difflib import SequenceMatcher
import sys


def separateFields( card ):

    return card.split("\t")


def cleanCard( card ):

    return re.sub( "\[\[[\w*]\]\]","",card )


def getWordAndPlural( field ):
    words = field.split(" ")
    print(words)
    return words[1], words[4]


def checkIfWordsAreSimilar( first, second ):
    if( SequenceMatcher( None, first, second ).ratio() > 0.5 and first[0]==second[0] and first[1]==second[1] and first[2]==second[2] ):
        return True
    else:
        return False

#TODO: bug fix: some words dont have plural
if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    parsed_file = open("parsed.txt", 'w+')

    for line in input_file.readlines():
        cleanLine = cleanCard(line)
        secondField= separateFields(cleanLine)[1]
        singular, plural = getWordAndPlural( secondField )
        if( checkIfWordsAreSimilar(singular, plural) ):
            parsed_file.write(cleanLine)
            #parsed_file.write("\n")
        else:
            pass

    parsed_file.close()
    input_file.close()