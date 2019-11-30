import os
import conversion
from flask import Flask, render_template, url_for, request, redirect, send_file

#for file uploading
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'pdf'}

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/media/legendary-acp/Development/Git/Intelligent-OCR-Scanner-Website/static/Uploads"

@app.route('/')

def index():
    return render_template('index.html', methods=['GET', 'POST'])

# For future development
# @app.route('/upload_doc')

# def return_file():
#     return send_file("/media/legendary-acp/Development/Git/Intelligent-OCR-Scanner-Website/static/Output/Output.txt", attachment_filename='Output.txt')

@app.route('/upload_doc', methods=[ 'POST'])

def upload_doc():
    if request.method == "POST":
        if request.files:
            document = request.files["document"]
            if document.content_type == "application/pdf":
                document.save(os.path.join(app.config['UPLOAD_FOLDER'] , document.filename))
                conversion.pdf2docx(app.config['UPLOAD_FOLDER'] + '/' + document.filename, app.config['UPLOAD_FOLDER'])
    return render_template('download.html', methods=['GET', 'POST'])