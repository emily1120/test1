from flask import Flask, request, render_template
import re

app = Flask(__name__)

#Validate ID number (assuming 台灣ID)
if len(id_number)!=10:
    return "身分證號碼應該為10碼" , 400
if not id_number[0].isalpha():
    return "第一個字元應該為英文字母碼" , 400
if not id_number[1:].isdigit():
    return "身分證號碼後九碼應為數字" , 400
#
@app.route('/')
def form():
    return render_template('intro.html')#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80
