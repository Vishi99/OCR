import cv2
import sys
import pytesseract

if __name__ == '__main__':

  # Read image path from command line
  imPath = r'C:\Users\user\Desktop\test3.png'

  # Uncomment the line below to provide path to tesseract manually
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l eng --oem 1 --psm 3')

  # Read image from disk
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(im, config=config).encode("utf-8")

  # Print recognized text
  print(text)
