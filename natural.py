from xml.dom.minidom import Identified
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

keywords = {"False", "await", "else", "import", "pass", "None", "break", "except", "raise", "True", "class", "finally", "is", "return", "and", "continue",
            "for", "lambda", "try", "as", "def", "from", "global", "not", "with", "async", "elif", "if", "or", "yield", "nonlocal", "del", "assert", "while", }

operators = {"+", "-", "*", "/", "%", "**", "//", "=", "+=", "-=", "*=", "/=", "/=", "%=", "//=", "**=", "&=", "|=", "^=", ">>=",
             "<<=", "==", "!=", ">", "<", ">=", "<=", "and", "or", "not", "is", "is not", "not in", "&", "|", "^", "~", "<<", ">>"}

delimiters = {'(', ')', '{', '}', '[', ']', '"', "'", ';', '#', ',', ''}


def detect_keywords(text):
    arr = []
    for word in text:
        if word in keywords:
            arr.append(word)
    return list(set(arr))


def detect_operators(text):
    arr = []
    for word in text:
        if word in operators:
            arr.append(word)
    return list(set(arr))


def detect_delimiters(text):
    arr = []
    for word in text:
        if word in delimiters:
            arr.append(word)
    return list(set(arr))


def detect_num(text):
    arr = []
    for word in text:
        try:
            a = int(word)
            arr.append(word)
        except:
            pass
    return list(set(arr))


def detect_identifiers(text):
    k = detect_keywords(text)
    o = detect_operators(text)
    d = detect_delimiters(text)
    n = detect_num(text)
    not_ident = k + o + d + n
    arr = []
    for word in text:
        if word.isidentifier():
            if word not in arr:
                if word not in not_ident:
                    arr.append(word)
    return arr


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['analisis']
    text_split = text.split()
    return render_template('form.html', variable=text, keyword=detect_keywords(text_split), operator=detect_operators(text_split), delimiter=detect_delimiters(text_split), identifiers=detect_identifiers(text_split), number=detect_num(text_split))


@app.errorhandler(404)
def internal_error(error):
    return redirect(url_for('my_form'))


if __name__ == '__main__':
    app.run(debug=True)
