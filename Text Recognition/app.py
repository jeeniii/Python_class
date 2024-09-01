import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

script_dir = os.path.dirname(os.path.abspath(__file__)) # app.py가 있는 절대 경로
image_path = os.path.join(script_dir, '쿠팡영수증.jpg') # app.py가 있는 절대 경로에서 '쿠팡영수증.jpg' 찾기

openedImage = Image.open(image_path)
results = pytesseract.image_to_string(openedImage, lang='kor')
print(script_dir)
print(results)

# import os
# print(os.getcwd())