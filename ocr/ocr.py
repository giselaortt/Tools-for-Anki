from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re


#TODO: checar se xist
def convertImageToGrayScale( path_to_image, output_name ):
    image = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(output_name, image)


def imageFromPdf( pdf_path, output_folder, pages_required = None ):
    images = convert_from_path(pdf_path)
    for i in range(len(images)):
        if( pages_required is None or i in pages_required ):
            images[i].save(output_folder + "/" + str(i+1) +'.jpg', 'JPEG')


def txtFromImage( image_path, output_name ):
    file_ptr=open( removeExtentionFromString(output_name)+".txt", "w")
    text = pytesseract.image_to_string(Image.open(image_path))
    file_ptr.write( text )
    file_ptr.close()


def removeExtentionFromString( text ):

    return re.sub( "\..{3}", "", text )


def applyFunctionThroughWholeFolder( input_path, output_path, function ):
    filenames = os.listdir(input_path)
    for file_name in filenames:
        function(input_path+"/"+file_name, output_path+"/"+file_name)


#TODO: PDF's need a diferent aproach, they need to have a new folder per input file. otherwise the code will overwrite the pages.
if __name__ == '__main__':
    path_to_pdf = "pdfs/Prufungstraining_Goethe-Zertifikat_C1.pdf"
    path_to_texts_folder = "extracted_txts"
    os.system("mkdir images")
    os.system("mkdir gray_images")
    path_to_images = "images"
    path_to_gray = "gray_images"

    imageFromPdf( path_to_pdf, path_to_images )
    applyFunctionThroughWholeFolder( path_to_images, path_to_gray, convertImageToGrayScale )
    applyFunctionThroughWholeFolder( path_to_gray, path_to_texts_folder, txtFromImage )

    #os.system("rm -r images gray_images")
