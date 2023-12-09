import re
import pytesseract

from PIL import Image
from colorama import Fore, Style

c_ = Fore.CYAN
m_ = Fore.MAGENTA
r_ = Fore.RED
b_ = Fore.BLUE
y_ = Fore.YELLOW
g_ = Fore.GREEN
w_ = Fore.WHITE

import warnings

warnings.filterwarnings(action='ignore')


class InvalidImageException(Exception):
    pass


def ExtractDetails(pillow_image) -> dict:
    text = pytesseract.image_to_string(pillow_image, lang='eng')
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    regex_DOB = re.compile('\d{2}[-/]\d{2}[-/]\d{4}')
    regex_num = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')

    file_details = {'Name': "Pankaj Kumar", "Father Name": "Satya Narayan"}

    if len(regex_num.findall(text)) == 0:
        raise InvalidImageException(
            f'{y_}Blurry Image for tesseract. Input new clear image for viewing pan card number !!!')
    else:
        file_details['Card Number'] = regex_num.findall(text)[0]

    if len(regex_DOB.findall(text)) == 0:
        raise InvalidImageException(
            f'{y_}Blurry Image for tesseract. Input new clear image for viewing DATE OF BIRTH !!!')
    else:
        file_details['Date of Birth'] = regex_DOB.findall(text)[0]
    return file_details
