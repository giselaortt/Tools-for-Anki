import sys
import re


def removeBold( sentence ):

	return re.sub("<b>|</b>","", sentence)


#retorna se as sentences são iguais, depois de remover o negrito.
def areEqual( first, second ):

	return ( removeBold(first) == removeBold(second) )


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


#TODO
def addToTranslation():
    pass


#TODO: E quando houverem mais de duas palavras em negrito na mesma frase ?
def mergeCards( firstCard, secondCard ):
	firstSentence, firstTranslation =  separateFields( firstCard )
	secondSentence, secondTranslation = separateFields( secondCard )
	newSentence = transferBoldThroughSentences( firstSentence, secondSentence )
	#firstTranslation = whoIsBold(firstSentence) + "<b>:</b>" + firstTranslation
	#secondTranslation = whoIsBold(secondSentence) + "<b>:</b>" + secondTranslation
	#TODO: translations should include the word
	newTranslation = firstTranslation+", "+secondTranslation

	return newSentence+";"+newTranslation


def createBold(sentence):
	sentence = re.sub( "\[\[", "<b> ", line )
	sentence = re.sub( "]]", " </b>", line )

	return sentence


def shorterSentence( sentence ):
    subsentences = re.split("–|;|!|\.|'|\"|«|:|»|,", line)
    for subsentence in subsentences :
    	if '[[' in subsentence :
    		#line = subsentence + ";" + subsentences[-1]

    		return subsentence


def separateFields( card ):

    return card.split(";")


def shorterFirstField( card ):
    firstField, secondField = separateFields(card)
    firstField = shorterSentence(firstField)

    return firtField + ";" + secondField


if __name__ == "__main__":
    fptr = open(sys.argv[1],'r')
    ans = open("parsed.txt", 'w+')
    otherfptr = open("no_repetition.txt", "a")
    otherfptr.write("\n")

    for line in fptr.readlines():
        line = shorterFirstField(line)
        line = createBold(line)
        ans.write(line)

    cards = ans.readlines()


    ans.close()
    fptr.close()
