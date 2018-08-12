try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print((pytesseract.image_to_string(Image.open(r'C:\Users\user\Desktop\test1.png'))).encode("utf-8"))
