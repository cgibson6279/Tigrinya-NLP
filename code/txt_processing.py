"""
txt_processing.py contains all the functions 
necessary to convert pdf texts to string texts

based on solutions provide in:
https://towardsdatascience.com/pdf-text-extraction-in-python-5b6ab9e92dd
"""
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def _convert_pdf_to_string(file_path):
    """
    convert_pdf_to_string is the generic text extractor code  
    copied from the pdfminer.six documentation,
    and slightly modified so we can use it as a function
    :param file_path:
    :return:
    """
    output_string = StringIO()

    with open(file_path, "rb") as in_file:

        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return output_string.getvalue()
