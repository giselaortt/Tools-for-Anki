import unittest
from parser import *


class TestParser( unittest.TestCase ):

    def test_removeBold(self):
        test = "<b>holen</b>"
        expected = "holen"
        self.assertEqual(removeBold(test), expected)


    def test_getFirstField(self):
        test = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch; schob sich auf dem Rücken langsam näher zum Bettpfosten, um den Kopf besser heben zu können\; fand die juckende Stelle, die mit lauter kleinen weißen Pünktchen besetzt war, die er ;buscar"
        expected = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch"
        self.assertEqual(getFirstField(test), expected)


    def test_createBold(self):
        test = "Der Teufel soll das alles [[holen]]"
        expected = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual(createBold(test), expected)


    def test_createBold_beginning_of_the_sentence(self):
        test = "[[holen]]"
        expected = "<b>holen</b>"
        self.assertEqual(createBold(test), expected)


    def test_firstFieldMatches(self):
        test = "this is a sentence;"
        self.assertTrue(firstFieldMatches(test, test))


    def test_firstFieldMatches_with_different_second_field(self):
        test = "this is a <b>sentence</b>; alguma coisa"
        other_test = "this <b>is</b> a sentence; etwas"
        self.assertTrue(firstFieldMatches(test, test))


    def test_firstFieldMatches_second_field_inexistent(self):
        test = "this is a sentence; alguma coisa"
        other_test = "this is a sentence;"
        self.assertTrue(firstFieldMatches(test, test))


    def test_firstFieldMatches_false(self):
        test = "this is a sentence;"
        other_test = "this is another sentence;"
        self.assertFalse( firstFieldMatches(test, other_test) )


    def test_whoIsBold_single_word( self ):
        test = "<b>holen</b>"
        self.assertEqual( whoIsBold(test), test )


    def test_whoIsBold( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual( whoIsBold(test), "<b>holen</b>" )


    def test_whoIsBold_no_bold( self ):
        test = "Der Teufel soll das alles holen"
        self.assertIsNone( whoIsBold(test) )


    def test_formatTranslationField( self ):
        test = "Der Teufel soll das alles <b>holen</b>;Esperar"
        expected = "Der Teufel soll das alles <b>holen</b>;<b>holen</b><b>: </b>Esperar"
        self.assertEqual(formatTranslationField(test), expected)


    def test_transferBoldThroughSentences( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        othertest = "Der <b>Teufel</b> soll das alles holen"
        expected = "Der <b>Teufel</b> soll das alles <b>holen</b>"
        self.assertEqual( transferBoldThroughSentences(test, othertest), expected )


    def test_transferBoldThroughSentences_equal_sentences( self ):
        test = "Der Teufel soll das alles <b>holen</b>"
        self.assertEqual( transferBoldThroughSentences(test, test), test )


    def test_mergeCards( self ):
        test = "Der Teufel soll das alles <b>holen</b>;buscar"
        othertest = "Der <b>Teufel</b> soll das alles holen;demonio"
        expected = "Der <b>Teufel</b> soll das alles <b>holen</b>;<b>holen</b><b>: </b>buscar,<b>Teufel</b><b>: </b>demonio"
        self.assertEqual( mergeCards(test,othertest), expected )


    def test_removeRepetitions_length_one_array( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;buscar"]
        self.assertEqual( removeRepetitions(test), test )


    def test_removeRepetitions_length_zero_array( self ):
        test = []
        self.assertEqual( removeRepetitions(test), test )


    def test_removeRepetitions_same_sentence( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;buscar","Der Teufel soll das alles <b>holen</b>;buscar" ]
        expected = ["Der Teufel soll das alles <b>holen</b>;<b>holen</b><b>: </b>buscar,<b>holen</b><b>: </b>buscar"]
        self.assertEqual( removeRepetitions(test), expected )


    def test_removeRepetitions( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;buscar","Der <b>Teufel</b> soll das alles holen;demonio" ]
        expected = ["Der <b>Teufel</b> soll das alles <b>holen</b>;<b>holen</b><b>: </b>buscar,<b>Teufel</b><b>: </b>demonio"]
        self.assertEqual( removeRepetitions(test), expected )


    def test_removeRepetitions_three_repetitions( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;buscar","Der <b>Teufel</b> soll das alles holen;demonio","Der Teufel soll <b>das</b> alles holen;o,a" ]
        expected = ["Der <b>Teufel</b> soll <b>das</b> alles <b>holen</b>;<b>holen</b><b>: </b>buscar,<b>Teufel</b><b>: </b>demonio,<b>das</b><b>: </b>o,a"]
        self.assertEqual( removeRepetitions(test), expected )


    def test_removeRepetitions_no_repetition( self ):
        test = ["Der Teufel soll das alles <b>holen</b>;buscar","Der <b>Teufel</b> soll das alles holen;demonio","Der Teufel soll <b>das</b> alles holen;o,a" ]
        expected = ["Der <b>Teufel</b> soll <b>das</b> alles <b>holen</b>;<b>holen</b><b>: </b>buscar,<b>Teufel</b><b>: </b>demonio,<b>das</b><b>: </b>o,a"]
        self.assertEqual( removeRepetitions(test), expected )


    def test_shortenFirstField( self ):
        test = "Der Teufel soll das alles [[holen]]!« Er fühlte ein leichtes Jucken oben auf dem Bauch\; schob sich auf dem Rücken langsam näher zum Bettpfosten, um den Kopf besser heben zu können\; fand die juckende Stelle, die mit lauter kleinen weißen Pünktchen besetzt war, die er ;buscar"
        expected = "Der Teufel soll das alles [[holen]];buscar"
        self.assertEqual(shortenFirstField(test), expected)


if __name__ == '__main__':
    unittest.main()
