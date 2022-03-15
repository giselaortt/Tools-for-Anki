# Tools for Anki desktop app

### Readlang_to_anki
this script parses the files from [Readlang](https://readlang.com/) website in order to create a better importation on [Anki](https://apps.ankiweb.net/) desktop application, and save many hours of my time.


## TODO:
- This folder grew too big and requires now a deep refactor.


### Context:
  - Anki is a Spaced Repetition System, wich I use every day to learn and practice new languages. 
  - Readlang is an website and chrome extention. It provides an interface to automatically translate unknown words from a foreign language by clicking on them while reading, and save all the unknown words to a database.

### Motivation:
  Both applications are really useful to learn languages, and belong to my routine of studies, however, Readlang does not provide a good importation system. It does export the new words to a .txt file, but has many problems. 
  Through this integration I can easily and automatically create new anki flashcards while reading content in Readlang, a process that I used to do manually up to now
  
  
### Folders:
 - eliminate_repetitions: I downloaded the deck from frequency dictionary of german. but my german is already b2, therefore many word sare useless to me. so with this code I could delete the words that were into my other deck and merge the 2 without so much manual work.
 - ocr: REadlang does not work on PDF's for now. I wanted to read the model tests from each language while saving the unknown words, So I am using OCR to extract the texts from those tests. This could become a Readlang for PDF one day.
 - parsers_deutsch_nouns:
 - readlang_intgration: This is a parser. It changes the formatting from readlang in order to make it a nicer view for ANKI and adds the translation from google translator automatically. Because the translation from google is a web request, It does take a long time to run this code. For 10 flashcards It might take 5 minutes. You can turn off the automatic translator if you need speed. I might turn this into an ANKI-addon on the future.
  
 
### Implemented:
  - Merges repeted sentences
  - Format the new learned word of the sentence with html bold.
  - it shortens the readlang sentences. Readlang exports flashcards way too long, making learning monotonous and slow, sometimes includding several sentences in the same field. Here I get the shortest sentence possible.
  - adds the word in the foreing language by the side of the readlang Translation.
  - Integration with google translate in order to add the whole sentence translated to my flashcards automatically.
  - Sort the order of words in sentences with several words selected
  - a parser for this Anki [dataset](https://ankiweb.net/shared/info/1852912768) It excludes bad entrances!
  - extract text from the PDF's of the Goethe-tests and book with model tests using OCR
  - estimation of my total german vocabulary
  - plural and gender correctedness checking with crawler and scrapping.
  - Eliminate repetitions: Add new flashcards to anki only if they are not already contained in the current deck.

### To be implemented:
  - better control for the size of the setences, not to end up with 1 word sentences.
  - Easier change of language. Currently contains only german to portuguese.
  - Add TTS with google API
  - getting highlighted words from images from website


