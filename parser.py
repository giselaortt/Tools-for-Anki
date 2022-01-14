import sys
import re
import os
from googletrans import Translator

translator = Translator()

def removeBold( sentence ):

    return re.sub("<b>|</b>","", sentence)


def createBold( sentence ):
    sentence = re.sub( "\[\[", "<b>", sentence )
    sentence = re.sub( "]]", "</b>", sentence )

    return sentence


def removeBold( sentence ):
    sentence = re.sub("<b>|</b>", "", sentence)

    return sentence


def separateFields( card ):

    return card.split(";")


def getFirstField( card ):

    return card.split(";")[0]


def firstFieldMatches( first, second ):
    first = getFirstField( first )
    second = getFirstField( second )

    return ( removeBold(first) == removeBold(second) )


def joinFields( first, second ):

    return first + ";" + second


def transferBoldThroughSentences( first, second ):
    one = first.split(" ")
    two = second.split(" ")
    for word, i in zip(two, range(len(two))):
        if( "<b>" in word ):
            one[i] = word

    return ' '.join(one)


def whoIsBold( sentence ):
    listOfWords = sentence.split(" ")
    for word in listOfWords:
        if("<b>" in word):

            return word


#I decided to substitute the Readlang translation for the googletrans version, because Readlang includes several errors.
def substituteTranslationOfTheWord( card ):
    sentence, _ = separateFields(card)
    word = whoIsBold(sentence)
    word = removeBold( word )
    translated = translator.translate(word, src='de', dest='pt')

    return joinFields(sentence,translated.text)


def formatTranslatedField( card ):
    sentence, translated = separateFields(card)
    word = whoIsBold(sentence)
    translated = word + "<b>: </b>" + translated

    return joinFields(sentence,translated)


def mergeCards( firstCard, secondCard ):
    firstSentence, firstTranslated =  separateFields( firstCard )
    secondSentence, secondTranslated = separateFields( secondCard )
    newSentence = transferBoldThroughSentences( firstSentence, secondSentence )
    newTranslated = firstTranslated.strip(" ")+", "+secondTranslated

    return joinFields( newSentence, newTranslated )


def shortenFirstField( sentence ):
    subsentences = re.split("–|;|!|\.|'|\"|«|:|»|,", sentence)
    for subsentence in subsentences :
        if '[[' in subsentence :

            return subsentence.strip(" ") + ";" + subsentences[-1]


#sometimes having the words translated are not enough.
def addHoleSentenceTranslation( card ):
    sentence, translations = separateFields(card)
    #translator = Translator()
    sentenceTranslation = translator.translate(sentence, src='de', dest='pt')
    translations = translations + "<br>" + sentenceTranslation.text

    return joinFields(sentence,translations)


def removeRepetitions( cards ):
    for i in range( len(cards)-1, -1, -1 ):
        for j in range( len(cards)-1, i, -1 ):
            if( firstFieldMatches( cards[i], cards[j] ) ):
                cards[i]=cards[i].strip("\n")
                cards[j]=cards[j].strip("\n")
                cards[i] = mergeCards( cards[i], cards[j] )+"\n"
                del cards[j]

    return cards


if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    parsed_file = open("parsed.txt", 'w+')
    no_repetition = open("without_repetition.txt", "w")

    #change from line to line to all lines at once
    for line in input_file.readlines():
        if(line == "\n"):
            continue
        line = re.sub("\n", " ", line)
        line = line.strip("\n")
        line = shortenFirstField(line)
        line = createBold(line)
        line = substituteTranslationOfTheWord(line)
        line = formatTranslatedField(line)
        line = addHoleSentenceTranslation(line)
        parsed_file.write(line)
        parsed_file.write("\n")

    parsed_file.seek(0)
    cards = parsed_file.readlines()
    cards = removeRepetitions(cards)

    for card in cards:
        no_repetition.write(card)

    os.remove("parsed.txt")
    no_repetition.close()
    parsed_file.close()
    input_file.close()
