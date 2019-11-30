#for pdf2text
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#for text2pdf
from docx import Document
from docx.shared import Inches

def pdf2text(fname):
    pagenums = set()
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def text2docx(text,path):
    document = Document()
    document.add_paragraph(text)
    document.save(path + '/' + "output.docx")

def text2file(text):
    file = open("/media/legendary-acp/Development/Git/Intelligent-OCR-Scanner-Website/static/Output/output.txt","w+")
    file.write(text)
    file.close() 


def pdf2docx(pathl,path):
    text = pdf2text(pathl)
    #text2docx(text,path)
    text2file(text)


#pdf2docx("/media/legendary-acp/Development/Git/Intelligent-OCR-Scanner-Website/static/Uploads/DBMS_Syllabus.pdf", "/media/legendary-acp/Development/Git/Intelligent-OCR-Scanner-Website/static/Uploads")