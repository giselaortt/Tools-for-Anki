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


def areLettersEqualWithTrema( word, secondWord, n ):
    if( (word[n] == "Ä" and secondWord[n] == "A") or (word[n] == "A" and secondWord[n] == "Ä") ):
        return True
    if( (word[n] == "Ë" and secondWord[n] == "E") or (word[n] == "E" and secondWord[n] == "Ë") ):
        return True
    if( (word[n] == "ä" and secondWord[n] == "a") or (word[n] == "a" and secondWord[n] == "ä") ):
        return True
    if( (word[n] == "ë" and secondWord[n] == "e") or (word[n] == "e" and secondWord[n] == "ë") ):
        return True
    if( (word[n] == "o" and secondWord[n] == "ö") or (word[n] == "ö" and secondWord[n] == "o") ):
        return True
    if( (word[n] == "Ö" and secondWord[n] == "O") or (word[n] == "O" and secondWord[n] == "Ö") ):
        return True

    return False


def areWordsSimilar( first, second ):

    return (SequenceMatcher( None, first, second ).ratio() > 0.5)


def doesInitialLettersMatch( first, second ):
    if((first[0]==second[0] or areLettersEqualWithTrema(first, second, o) ) and (first[1]==second[1] or areLettersEqualWithTrema(first,second,1) )):

        return True


def areWordsPlural( first, second ):

    return (areWordsSimilar( first, second ) and doesInitialLettersMatch( first, second ))


def fieldIncludePlural( field ):

    return re.search( ",", field )


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