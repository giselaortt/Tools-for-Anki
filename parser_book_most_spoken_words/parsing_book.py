import re
import fitz
import sys


def extract_text_from_pdf( pdf_file ):
    text = ""
    for page in pdf_file:
        text += page.get_text()

    return text


def open_pdf( name ):

    return fitz.open(name)


def remove_page_mark( text ):
    pass


def parse_text( text ):
    pass


def formatting_fields():
    pass


def extract_fields():
    pass


def split_per_word():
    pass


def split_text_per_sections():
    pass


if __name__ == "__main__":
    pdf_file = open_pdf(sys.argv[1])
    output_file = open(sys.argv[2],'w')

    txt = extract_text_from_pdf( pdf_file )
    output_file.write(txt)

    pdf_file.close()
    output_file.close()