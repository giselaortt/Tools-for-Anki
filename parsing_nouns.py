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


#TODO: improve the method to find who is plural
def checkIfWordsAreSimilar( first, second ):
    if( SequenceMatcher( None, first, second ).ratio() > 0.5 ):
        return True
    else:
        return False


def fieldIncludePlural( field ):

    return re.search( " , ", field )


def isFormattingCompliant( field ):
    if( len(field.split(" ")) == 5 ):
        return True
    else:
        return False


def createThirdField( secondField ):
    splited = secondField.strip(" \n").split(" ")
    thirdField = splited[-1]
    secondField = ' '.join( splited[0:-1] )

    return secondField, thirdField


def joinFields( firstField, secondField, thirdField ):

    return ";".join([firstField.strip(" "), secondField.strip(" "), thirdField.strip(" ")])+"\n"


#TODO: Refactor
if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    parsed_file = open("parsedNouns.txt", 'w')
    excluded = open("excluded.txt", "w")

    for line in input_file.readlines():
        cleanLine = cleanCard(line)
        firstField, secondField = separateFieldsWithTab(cleanLine)
        secondField, thirdField = createThirdField( secondField )
        answer = joinFields( firstField, secondField, thirdField )
        if( isFormattingCompliant( secondField )  ):
            if( fieldIncludePlural( secondField ) ):
                word, plural = getWordAndPlural( secondField )
                if( checkIfWordsAreSimilar( word, plural ) ):
                    parsed_file.write(answer)
                else:
                    excluded.write(answer)
            else:
                parsed_file.write(answer)
        else:
            excluded.write(answer)

    parsed_file.close()
    input_file.close()
    excluded.close()