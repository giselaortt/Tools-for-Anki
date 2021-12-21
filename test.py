import unittest
from parser import *


class TestParser( unittest.TestCase ):

    def test_removeBold(self):
        test = "<b>holen</b>"
        expected = "holen"
        self.assertEqual(removeBold(test), expected)


    def test_createBold(self):
        test = "Der Teufel soll das alles [[holen]]"
        expected = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual(createBold(test), expected)


    def test_createBold_beginning_of_the_sentence(self):
        test = "[[holen]]"
        expected = "<b>holen</b>"
        self.assertEqual(createBold(test), expected)

    def test_firstFieldMatches(self):
        pass


    def test_whoIsBold( self ):
        pass


    def test_formatTranslationField( self ):
        pass


    def test_mergeCards( self ):
        pass


    def test_shortenFirstField( self ):
        pass


if __name__ == '__main__':
    unittest.main()
