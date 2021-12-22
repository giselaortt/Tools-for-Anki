import sys
import re

def removeBold( sentence ):

    return re.sub("<b>|</b>","", sentence)


def createBold(sentence):
    sentence = re.sub( "\[\[", "<b>", sentence )
    sentence = re.sub( "]]", "</b>", sentence )

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


def formatTranslatedField( card ):
    sentence, Translated = separateFields(card)
    word = whoIsBold(sentence)
    Translated = word + "<b>: </b>" + Translated

    return joinFields(sentence,Translated)


def mergeCards( firstCard, secondCard ):
    firstSentence, firstTranslated =  separateFields( firstCard )
    secondSentence, secondTranslated = separateFields( secondCard )
    newSentence = transferBoldThroughSentences( firstSentence, secondSentence )
    newTranslated = firstTranslated+", "+secondTranslated

    return joinFields( newSentence, newTranslated )


def shortenFirstField( sentence ):
    subsentences = re.split("–|;|!|\.|'|\"|«|:|»|,", sentence)
    for subsentence in subsentences :
        if '[[' in subsentence :
            #line = subsentence + ";" + subsentences[-1]

            return subsentence + ";" + subsentences[-1]


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

    for line in input_file.readlines():
        if(line == "\n"):
            continue
        line = re.sub("\n", " ", line)
        line = line.strip("\n")
        line = shortenFirstField(line)
        line = createBold(line)
        line = formatTranslatedField(line)
        parsed_file.write(line)
        parsed_file.write("\n")

    parsed_file.seek(0)
    cards = parsed_file.readlines()
    cards = removeRepetitions(cards)

    for card in cards:
        no_repetition.write(card)

    no_repetition.close()
    parsed_file.close()
    input_file.close()
