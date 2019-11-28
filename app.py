from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html', methods=['GET', 'POST'])

@app.route('/upload_doc', methods=[ 'POST'])

def upload_doc():
    if request.method == "POST":
        if request.files:
            document = request.files["document"]
            if document.content_type == "application/pdf":
                print(document.content_type)
    return render_template('download.html', methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True)