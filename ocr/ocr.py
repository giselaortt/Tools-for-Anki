from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import argparse
import cv2
import os


def convertImageToGrayScale( path_to_image, output_path ):
    image = cv2.imread(args["path_to_image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray)


def imageFromPdf( pdf_path, output_folder, pages_required = None ):
    images = convert_from_path('example.pdf')
    for i in range(len(images)):
        if pages_required not None and i in pages_required :
            images[i].save(output_folder + str(i+1) +'.jpg', 'JPEG')


#TODO: add preprocessing steps
def txtFromImage( image_path, output_path ):
    file_ptr=open(output_path)
    text = pytesseract.image_to_string(Image.open(filename))
    file_ptr.write( text )
    file_ptr.close()
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


def applyFunctionThroughWholeFolder( input_path, output_path, function ):
    filenames = os.listdir(input_path)
    for file_name in filenames:
        function(input_path+file_name, output_path+file_name)


#TODO: PDF's need a diferent aproach, they need to have a new folder per input file. otherwise the code will overwrite the pages.
if __name__ == '__main__'():
    path_to_pdf = "pdfs"
    path_to_texts_folder = "extracted_txts"
    os.system("mkdir images")
    os.system("mkdir gray_images")
    path_to_images = "images"
    path_to_gray = "gray"

    imageFromPdf( path_to_pdf, path_to_images )
    applyFunctionThroughWholeFolder( path_to_images, path_to_gray, convertImageToGrayScale )
    applyFunctionThroughWholeFolder( path_to_gray, extracted_txts )

    os.system("rm -r images gray_images")
