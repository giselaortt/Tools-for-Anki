import unittest
from parsing_from_readlang import *
from parsing_nouns import *

#TODO: rename de functions
class TestParser( unittest.TestCase ):

    def testRemoveBold(self):
        test = "<b>holen</b>"
        expected = "holen"
        self.assertEqual(removeBold(test), expected)


    def testCreateBold(self):
        test = "Der Teufel soll das alles [[holen]]"
        expected = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual(createBold(test), expected)


    def testGetFirstField(self):
        test = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch; schob sich auf dem Rücken langsam näher zum Bettpfosten, um den Kopf besser heben zu können\; fand die juckende Stelle, die mit lauter kleinen weißen Pünktchen besetzt war, die er ;buscar"
        expected = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch"
        self.assertEqual(getFirstField(test), expected)


    def testFirstFieldMatches(self):
        test = "this is a sentence;"
        self.assertTrue(firstFieldMatches(test, test))


    def testCreateBoldbeginningOfTheSentence(self):
        test = "[[holen]]"
        expected = "<b>holen</b>"
        self.assertEqual(createBold(test), expected)


    def testFirstFieldMatchesWithDifferentSecondField(self):
        test = "this is a <b>sentence</b>; alguma coisa"
        other_test = "this <b>is</b> a sentence; etwas"
        self.assertTrue(firstFieldMatches(test, test))


    def testFirstFieldMatchesSecondFieldInexistent(self):
        test = "this is a sentence; alguma coisa"
        other_test = "this is a sentence;"
        self.assertTrue(firstFieldMatches(test, test))


    def testFirstFieldMatchesFalse(self):
        test = "this is a sentence;"
        other_test = "this is another sentence;"
        self.assertFalse( firstFieldMatches(test, other_test) )


    def testWhoIsBoldSingleWord( self ):
        test = "<b>holen</b>"
        self.assertEqual( whoIsBold(test), test )


    def testWhoIsBold( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual( whoIsBold(test), "<b>holen</b>" )


    def testWhoIsBoldNoBold( self ):
        test = "Der Teufel soll das alles holen"
        self.assertIsNone( whoIsBold(test) )


    def testFormatTranslatedField( self ):
        test = "Der Teufel soll das alles <b>holen</b>;Esperar"
        expected = "Der Teufel soll das alles <b>holen</b>;<b>holen</b><b>: </b>Esperar"
        self.assertEqual(formatTranslatedField(test), expected)


    def testTransferBoldThroughSentences( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        othertest = "Der <b>Teufel</b> soll das alles holen"
        expected = "Der <b>Teufel</b> soll das alles <b>holen</b>"
        self.assertEqual( transferBoldThroughSentences(test, othertest), expected )


    def testTransferBoldThroughSentencesEqualSentences( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual( transferBoldThroughSentences(test, test), test )


    def testMergeCards( self ):
        test = "Der Teufel soll das alles <b>holen</b>; holen: buscar"
        othertest = "Der <b>Teufel</b> soll das alles holen; Teufel: demonio"
        expected = "Der <b>Teufel</b> soll das alles <b>holen</b>;Teufel: demonio, holen: buscar"
        self.assertEqual( mergeCards(test,othertest), expected )


    def testRemoveRepetitionsLengthOneArray( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;holen: buscar"]
        self.assertEqual( removeRepetitions(test), test )


    def testRemoveRepetitionsLengthZeroArray( self ):
        test = []
        self.assertEqual( removeRepetitions(test), test )


    def testRemoveRepetitionsSameSentence( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;holen: buscar","Der Teufel soll das alles <b>holen</b>;holen: buscar"]
        expected = ["Der Teufel soll das alles <b>holen</b>;holen: buscar, holen: buscar\n"]
        self.assertEqual( removeRepetitions(test), expected )

    def testRemoveRepetitions( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;holen: buscar","Der <b>Teufel</b> soll das alles holen;Teufel: demonio" ]
        expected = ["Der <b>Teufel</b> soll das alles <b>holen</b>;Teufel: demonio, holen: buscar\n"]
        self.assertEqual( removeRepetitions(test), expected )


    def testRemoveRepetitionsWithThreeRepetitions( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;holen: buscar","Der <b>Teufel</b> soll das alles holen; Teufel: demonio","Der Teufel soll <b>das</b> alles holen; o: a" ]
        expected = ["Der <b>Teufel</b> soll <b>das</b> alles <b>holen</b>;o: a, Teufel: demonio, holen: buscar\n"]
        self.assertEqual( removeRepetitions(test), expected )


    def testRemoveRepetitionsNoRepetition( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;holen: buscar","Der <b>Teufel</b> soll das alles holen; Teufel: demonio","Der Teufel soll <b>das</b> alles holen; o: a" ]
        expected = ["Der <b>Teufel</b> soll <b>das</b> alles <b>holen</b>;o: a, Teufel: demonio, holen: buscar\n"]
        self.assertEqual( removeRepetitions(test), expected )


    def testShortenFirstField( self ):
        test = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch\ und schob sich auf dem Rücken langsam näher zum Bettpfosten, um den Kopf besser heben zu können;holen: buscar"
        expected = "Der Teufel soll das alles [[holen]];holen: buscar"
        self.assertEqual(shortenFirstField(test), expected)


    def testSubstituteTranslationOfTheWord( self ):
        test = "Der Teufel soll das alles <b>holen</b>;wrong"
        expected = "Der Teufel soll das alles <b>holen</b>;buscar"
        self.assertEqual(expected, substituteTranslationOfTheWord(test) )


    def testRemoveBold( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        expected = "Der Teufel soll das alles holen"
        self.assertEqual(expected, removeBold(test))


    def testGetWordFromTranslationField( self ):
        test = "<b>Aussichten</b><b>: </b>panorama<br>as <b> perspectivas </b> para o futuro"
        expected = "Aussichten"
        self.assertEqual( getWordFromTranslationField(test), expected )


    def testGetPositionsOfWordsInSentence( self ):
        pass


    def testGlueTranslations( self ):
        pass


    def testGlueTranslationFieldsInOrder( self ):
        testSentence = "Der <b>Teufel</b> soll das alles <b>holen</b>;"
        testFirstTranslationField = " holen: buscar"
        testSecondTranslationField = " Teufel: demonio"
        expected = "Teufel: demonio, holen: buscar"
        self.assertEqual( glueTranslationFieldsInOrder(testSentence, testFirstTranslationField, testSecondTranslationField), expected )


    def testGlueTranslationFieldsInOrderWith3Translations( self ):
        testSentence = "Der <b>Teufel</b> soll das <b>alles</b> <b>holen</b>;"
        testFirstTranslationField = " holen: buscar"
        testSecondTranslationField = "alles: todos, Teufel: demonio"
        expected = "Teufel: demonio, alles: todos, holen: buscar"
        self.assertEqual( glueTranslationFieldsInOrder(testSentence, testFirstTranslationField, testSecondTranslationField), expected )


    def testCleanCard( self ):
        testeCard = "Hand [anki:play:q:0]	Die Hand , Die Hände Hand [anki:play:a:0]"
        expected = "Hand 	Die Hand, Die Hände Hand"
        self.assertEqual( cleanCard(testeCard), expected )


    def testSeparateFieldsWithTab( self ):
        test = "Auge	Das Auge , Die Augen Eye"
        expected = ['Auge', 'Das Auge , Die Augen Eye']
        self.assertEqual( separateFieldsWithTab(test), expected )


    def testAreLettersEqualWithTrema( self ):
        self.assertTrue( areLettersEqualWithTrema("ü", "u") )
        self.assertTrue( areLettersEqualWithTrema("ö", "o") )
        self.assertTrue( areLettersEqualWithTrema("ë", "e") )


    def testDoesInitialLettersMatch( self ):
        self.assertTrue( doesInitialLettersMatch('Wurf', 'Würfe'))


    def testAreWordsPlural( self ):
        word = "Man"
        plural = "Männer"
        self.assertTrue( areWordsPlural(word, plural) )
        word = "Rad"
        plural = "Räder"
        self.assertTrue( areWordsPlural(word,plural) )


if __name__ == '__main__':
    unittest.main()