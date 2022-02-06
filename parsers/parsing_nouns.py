import re
from difflib import SequenceMatcher
import sys
from unidecode import unidecode


def separateFieldsWithTab( card ):

    return card.split("\t")


def cleanExtraSpaces( field ):
    field = re.sub(",",", ", field)
    field = re.sub(" {2,}", " ", field).strip()
    field = re.sub(" ,",",", field)

    return field


def cleanAnkiInformation( card ):

    return re.sub( "\[.{12,13}]","",card )


def cleanCard( card ):
    card = cleanAnkiInformation(card)
    card = cleanExtraSpaces(card)
    card = card.strip("\n")

    return card


def isArticle( word ):

    return ( word=="der" or word=="die" or word=="das" )


def isFormattingCompliant( words ):
    if( not isArticle(words[0].lower()) ):
        return False

    if( len(words) != 4 and len(words) != 2 ):
        return False

    if( words[2].lower() != "die" ):
        return False

    if( words[1][-1] != "," ):
        return False

    return True


def improveFormatting( words ):
    pass


def getWordAndPlural( field ):
    words = re.sub(",","", field).split(" ")

    return words[1], words[3]


def createThirdField( secondField ):
    words = secondField.split(" ")
    thirdField = ' '.join( words[4:] )
    secondField = ' '.join( words[0:4] )

    return secondField, thirdField


def areLettersEqualWithTrema( char, otherChar ):

    return ( unidecode(char) == unidecode(otherChar) )


def doesInitialLettersMatch( first, second ):

    return (areLettersEqualWithTrema(first[0],second[0]) and  areLettersEqualWithTrema(first[1],second[1]))


def areWordsSimilar( first, second ):

    return (SequenceMatcher( None, unidecode(first).lower(), unidecode(second).lower() ).ratio() > 0.5)


def areWordsPlural( first, second ):

    return (areWordsSimilar( first, second ) and doesInitialLettersMatch( first, second ))


def fieldIncludePlural( field ):
    if( re.search( "---", field ) ):
        return False
    if( re.search(",", field) ):
        return True

    return False


def joinFields( firstField, secondField, thirdField ):

    return ";".join([firstField.strip(" "), secondField.strip(" "), thirdField.strip(" ")])+"\n"


if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    parsed_file = open("parsedNouns.txt", 'w')
    excluded = open("excluded.txt", "w")

    for line in input_file.readlines():
        cleanLine = cleanCard(line)
        firstField, secondField = separateFieldsWithTab(cleanLine)
        secondField, thirdField = createThirdField( secondField )
        answer = joinFields( firstField, secondField, thirdField )

        if( not fieldIncludePlural( secondField )  ):
            parsed_file.write(answer)
            continue

        if( isFormattingCompliant( secondField.split(" ") ) ):
            word, plural = getWordAndPlural( secondField )
            if( areWordsPlural( word, plural ) ):
                parsed_file.write(answer)

    parsed_file.close()
    input_file.close()
    excluded.close()