from flask import Flask,request,jsonify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import io

app = Flask(__name__)

@app.route('/encrypt',methods=['POST'])
def encrypt():

    file = request.files['image']
    key = request.form['key'].encode()

    data = file.read()

    key = key.ljust(16)[:16]

    cipher = AES.new(key,AES.MODE_EAX)

    ciphertext,tag = cipher.encrypt_and_digest(data)

    return jsonify({"message":"Image Encrypted Successfully"})

@app.route('/decrypt',methods=['POST'])
def decrypt():

    return jsonify({"message":"Image Decrypted Successfully"})

if __name__=="__main__":
    app.run(debug=True)