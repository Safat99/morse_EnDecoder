from crypt import methods
from flask import render_template, request
from app import app

from morse_endecoder import encode, decode

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/encode", methods=['POST'])
def encoding():
    for_encoded = request.form.get('encode')
    encoded_form = encode(for_encoded)
    print(for_encoded)
    return render_template('encode.html', for_encoded = for_encoded, encoded_form = encoded_form)

@app.route("/decode", methods=['POST'])
def decoding():
    for_decoded = request.form.get('decode')
    decoded_form = decode(for_decoded)
    print(for_decoded)
    return render_template('decode.html', for_decoded = for_decoded, decoded_form = decoded_form)