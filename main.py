#147*83

import warnings

# Ignore the PendingDeprecationWarning
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)
from mpmath import mp
import pyautogui
from docx import Document
from process_img import *

if __name__ == '__main__':
    print("hello world!")
    mp.dps=12201
    text=str(mp.pi)

    rows=147
    column=83

    doc = Document()

    # Define the text and formatting
    font_size = 7
    font_colors = process()
    # Add paragraphs with different font sizes and colors
    p = doc.add_paragraph('A plain paragraph having some ')

    # Save the Word document
    doc.save("output.docx")



    # pyautogui.moveTo(400, 400, duration=2)
    # pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

