import sys
import re


def removeBold( sentence ):

	return re.sub("<b>|</b>","", sentence)


def separateFields( card ):

    return card.split(";")


def firstFieldMatches( first, second ):
    first, _ = separateFields( first )
    second, _ = separateFields( second )
	return ( removeBold(first) == removeBold(second) )


def uniteFields( first, second ):

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


def formatTranslationField( card ):
    sentence, translation = separateFields(card)
    word = whoIsBold(sentence)
    translation = word + "<b>: </b>" + translation

    return uniteFields(sentence,translation)


def mergeCards( firstCard, secondCard ):
	firstSentence, firstTranslation =  separateFields( firstCard )
	secondSentence, secondTranslation = separateFields( secondCard )
	newSentence = transferBoldThroughSentences( firstSentence, secondSentence )
	newTranslation = firstTranslation+", "+secondTranslation

	return uniteFields( newSentence, newTranslation )


def createBold(sentence):
	sentence = re.sub( "\[\[", "<b> ", line )
	sentence = re.sub( "]]", " </b>", line )

	return sentence


def shorterSentence( sentence ):
    subsentences = re.split("–|;|!|\.|'|\"|«|:|»|,", line)
    for subsentence in subsentences :
    	if '[[' in subsentence :
    		#line = subsentence + ";" + subsentences[-1]

    		return subsentence.strip(" ")


def shortenFirstField( card ):
    firstField, secondField = separateFields(card)
    firstField = shorterSentence(firstField)

    return firtField + ";" + secondField


if __name__ == "__main__":
    fptr = open(sys.argv[1],'r')
    ans = open("parsed.txt", 'w+')
    otherfptr = open("no_repetition.txt", "a")
    otherfptr.write("\n")

    for line in fptr.readlines():
        line = shortenFirstField(line)
        line = createBold(line)
        line = formatTranslationField(line)
        ans.write(line)

    cards = ans.readlines()
    for i in range( len(cards) ):
        for j in range( i+1, len(cards) ):
            if( firstFieldMatches( cards[i], cards[j] ) ):
                cards[i] = mergeCards( cards[i], cards[j] )
                cards.pop(j)

    for card in cards:
        otherfptr.write(cards)

    otherfptr.close()
    ans.close()
    fptr.close()
