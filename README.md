# Readlang_to_anki
this script parses the files from [Readlang](https://readlang.com/) website in order to create a better importation on [Anki](https://apps.ankiweb.net/) desktop application, and save many hours of my time.


### Context:
  - Anki is a Spaced Repetition System, wich I use every day to learn and practice new languages. 
  - Readlang is an website and chrome extention. It provides an interface to automatically translate unknown words from a foreign language by clicking on them while reading, and save all the unknown words to a database.

### Motivation:
  Both applications are really useful to learn languages, and belong to my routine of studies, however, Readlang does not provide a good importation system. It does export the new words to a .txt file, but has many problems. 
  Through this integration I can easily and automatically create new anki flashcards while reading content in Readlang, a process that I used to do manually up to now.
  
### Implemented:
  - Merges repeted sentences
  - Format the new learned word of the sentence with html bold.
  - it shortens the readlang sentences. Readlang exports flashcards way too long, making learning monotonous and slow, sometimes includding several sentences in the same field. Here I get the shortest sentence possible.
  - adds the word in the foreing language by the side of the readlang Translation.
  - Integration with google translate in order to add the whole sentence translated to my flashcards.
  - Sort the order of words in sentences with several words selected
  - OCR: extract text from the PDF's of the Goethe-tests.

### To be implemented:
  - Control for the size of the setences, not to end up with 1 word sentences.
  - Easier change of language. Currently contains only german to portuguese.
  - Add TTS with google API

## Problems:
  - Slow.

## Bonus!
  Implemented a parser for this Anki dataset: https://ankiweb.net/shared/info/1852912768
  It excludes bad entrances!
  - TODO: Implement plural correctedness checking with crawler and scrapping.


### How to use:
  You need to have python3 installed.
  
  Download the file parser.py to your computer. At Readlang, go to libery and export all your learned words. Through the terminal, access the location in witch you've downloaded the script, than run the script passing the file of the Readlang .txt though command line, for example:  `python3 parser.py 2021-12-19_ReadlangWords.txt`
  
  A new file will be created with the cards parsed. Import this new file in anki. You need to select "allow HTML in cards" option, and use ";" as a delimiter.
