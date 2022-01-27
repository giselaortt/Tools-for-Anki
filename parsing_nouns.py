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


#TODO: needs debugind
def areLettersEqualWithTrema( word, secondWord, n ):
    if( word[n] == "Ä" and secondWord[n] == "A" ):
        return True
    if( word[n] == "Ë" and secondWord[n] == "E" ):
        return True
    if( word[n] == "ä" and secondWord[n] == "a" ):
        return True
    if( word[n] == "ë" and secondWord[n] == "e" ):
        return True
    if( word[n] == secondWord[n] ):
        return True
    return False


#TODO: improve the method to find who is plural
def areWordsSimilar( first, second ):
    #se a primeira letra for igual ou igual com trema
    if( areLettersEqualWithTrema(first, second, 0) and areLettersEqualWithTrema(first, second,1) ):
        if( SequenceMatcher( None, first, second ).ratio() > 0.5 ):
            return True
        else:
            print( SequenceMatcher( None, first, second ).ratio(), first, second )
            return False
    else:
        return False


def fieldIncludePlural( field ):

    return re.search( " , ", field )


#TODO: debug
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
                if( areWordsSimilar( word, plural ) ):
                    parsed_file.write(answer)
                else:
                    excluded.write("reason:non plural  "+answer)
            else:
                parsed_file.write(answer)
        else:
            excluded.write("reason: non-compliant "+answer)

    parsed_file.close()
    input_file.close()
    excluded.close()