from werkzeug.exceptions import BadRequestKeyError

from flask import Flask, render_template, request, jsonify
from PIL import Image
import io

from ocr_extract import ExtractDetails

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/extract/info/', methods=['POST'])
def extract_information():
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            request_object_content = uploaded_file.read()
            pillow_image = Image.open(io.BytesIO(request_object_content))
            return jsonify(ExtractDetails(pillow_image))

        raise FileNotFoundError("Please upload PAN or Aadhar card image file.")
    except BadRequestKeyError:
        raise FileNotFoundError("Please upload PAN or Aadhar card image file.")


if __name__ == '__main__':
    app.run(debug=True)


"""
Blockchain:
1) Block
2) Blockchain
3) Hashed Algorithm
4) Mining
5) Nounce
6) Public Key and Private Key
7) Digital Signature Generation Algorithm
7) Digital Signature Verification Algorithm
"""