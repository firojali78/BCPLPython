import requests
import json
from requests_ntlm import HttpNtlmAuth
from flask import Flask, jsonify, request, render_template, redirect, url_for




# setting up flask app
app = Flask(__name__ , template_folder='templates')

#http://127.0.0.1:6262/checkBalance/V00803
@app.route('/checkBalance/<vendor_code>',methods=['GET','POST'])
def checkBalance(vendor_code):
    res = sendReq(vendor_code)
    return res

#http://127.0.0.1:6262/weblogin/C1114/1234/Distributor
@app.route('/weblogin/<username>/<password>/<logintype>',methods=['GET','POST'])
def weblogin(username,password,logintype):
    res = webuserlogin(username,password,logintype)
    return res

def sendReq(vendorcode):
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetVendorBalance?Company=Bodycare"

    req = "\"VendorCode\":\"{vendor_code}\""
    req = req.format(vendor_code=vendorcode)
    req = "{"+req+"}"



    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, auth=HttpNtlmAuth(url+"VMServer1\Ankit", "bcpl@123"))

    print(response.text)
    print(response.status_code)
    print(response.request.body)
    return response.json()

#function name Start +
def webuserlogin(username,password,logintype):
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetWebUserBCPL?Company=Bodycare"

    req = '\"UserID\":\"{user_name}\",\"Password\":\"{pass_word}\",\"LoginType\":\"{login_type}\"'
    req = req.format(user_name=username)
    req = req.format(pass_word=password)
    req = req.format(login_type=logintype)
    print(req)
    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.request("POST", url, headers=headers, data=payload, auth=HttpNtlmAuth(url+"VMServer1\Ankit", "bcpl@123"))

    print(response.text)
    return response.json()
#function name Start -

app.config["DEBUG"] = True

# starting flask application
if __name__ == '__main__':
    app.run(debug=True, port=6262)
    #app.run(host='192.168.1.44', port=6262, debug=True)
