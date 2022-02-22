# Tools for Anki desktop app

### Readlang_to_anki
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
  - Integration with google translate in order to add the whole sentence translated to my flashcards automatically.
  - Sort the order of words in sentences with several words selected
  - a parser for this Anki [dataset](https://ankiweb.net/shared/info/1852912768) It excludes bad entrances!
  - extract text from the PDF's of the Goethe-tests and book with model tests using OCR

### To be implemented:
  - better control for the size of the setences, not to end up with 1 word sentences.
  - Easier change of language. Currently contains only german to portuguese.
  - Add TTS with google API
  - plural and gender correctedness checking with crawler and scrapping.
  - getting highlighted words from images from website

## Problems:
  - Slow.

