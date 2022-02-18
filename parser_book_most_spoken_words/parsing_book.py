import re
import fitz


def formatting_fields():
    pass


def extract_fields():
    pass


def split_per_word():
    pass


def split_text_per_sections():
    pass


def extract_text_from_pdf( pdf_file ):
    text = ""
    for page in pdf_file:
        text += page.getText()

    return text


def remove_page_mark( text ):
    pass


def parse_text( text ):
    pass


def open_pdf( name ):

    return fitz.open(name)


if __name__ == "__main__":
    pdf_file = open_pdf(sys.argv[1],'r')
    output_file = open(sys.argv[2],'r')

    txt = extract_text_from_pdf( pdf_file )
    print( parse_text(txt) )

    pdf_file.close()
    output_file.close()