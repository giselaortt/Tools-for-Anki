import unittest
from parsing_nouns import *


class TestParser( unittest.TestCase ):

    def testAreLettersEqualWithTrema( self ):
        self.assertTrue( areLettersEqualWithTrema("ü", "u") )
        self.assertTrue( areLettersEqualWithTrema("ö", "o") )
        self.assertTrue( areLettersEqualWithTrema("ë", "e") )


    def testDoesInitialLettersMatch( self ):
        self.assertTrue( doesInitialLettersMatch('Wurf', 'Würfe'))


    def testCleanCard( self ):
        testeCard = "Hand [anki:play:q:0]	Die Hand , Die Hände Hand [anki:play:a:0]"
        expected = "Hand 	Die Hand, Die Hände Hand"
        self.assertEqual( cleanCard(testeCard), expected )


    def testSeparateFieldsWithTab( self ):
        test = "Auge	Das Auge , Die Augen Eye"
        expected = ['Auge', 'Das Auge , Die Augen Eye']
        self.assertEqual( separateFieldsWithTab(test), expected )


    def testAreWordsPlural( self ):
        word = "Man"
        plural = "Männer"
        self.assertTrue( areWordsPlural(word, plural) )
        word = "Rad"
        plural = "Räder"
        self.assertTrue( areWordsPlural(word,plural) )


if __name__ == '__main__':
    unittest.main()