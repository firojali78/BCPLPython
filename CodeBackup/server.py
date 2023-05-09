import requests
import json
from requests_ntlm import HttpNtlmAuth
from flask import Flask, jsonify, request, render_template, redirect, url_for


#validateuser

# setting up flask app
app = Flask(__name__ , template_folder='templates')

# -----------checkBalance For showing Public URL Start +
@app.route('/checkBalance/<vendor_code>',methods=['GET','POST'])
def checkBalance(vendor_code):
    res = sendReq(vendor_code)
    return res
# checkBalance For showing Public URL Start -

# -----------weblogin For showing Public URL Start +
@app.route('/weblogin/<username>/<password>/<logintype>',methods=['GET','POST'])
def weblogin(username,password,logintype):
    res = webuserlogin(username,password,logintype)
    return res
# weblogin For showing Public URL End -

# -----------webcredentialsvalidate For showing Public URL Start +
@app.route('/webcredentialsvalidate/<username>/<password>',methods=['GET','POST'])
def webcredentialsvalidate(username,password):
    res = credentialsvalidate(username,password)
    return res
# webcredentialsvalidate For showing Public URL End -

# -----------webitemListws For showing Public URL Start +
@app.route('/webitemlistws',methods=['GET','POST'])
def webitemlistws():
    res = itemlistws()
    return res
# webitemlistws For showing Public URL End -


# -----------webbarcodeprint For showing Public URL Start +
@app.route('/webbarcodeprint',methods=['GET','POST'])
def webbarcodeprint():
    if request.method == 'POST':
        input_json = request.get_json()
        #print(input_json)
        phylotno = input_json.get("PhyLotNo")
        itemno = input_json.get("ItemNo")
        variantcode = input_json.get("VariantCode")
        printreport = input_json.get("PrintReport")
        uom = input_json.get("UOM")
        issuedtouid = input_json.get("IssuedToUID")
        no0fbarcodes = input_json.get("No0fBarcodes")
        uommrp = input_json.get("UOMMRP")
        pricegroupcode = input_json.get("PriceGroupCode")
        purstndrdqty = input_json.get("PurStndrdQty")
        createdby = input_json.get("CreatedBy")
        res = barcodeprint(phylotno,itemno,variantcode,printreport,uom,issuedtouid,no0fbarcodes,uommrp,pricegroupcode,purstndrdqty,createdby)
        #return res
        return res.get("value")
# webbarcodeprint For showing Public URL End -


# -----------webvalidateuser For showing Public URL Start +
@app.route('/webvalidateuser',methods=['GET','POST'])
def webvalidateuser():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        username = input_json.get("UserID")
        res = validateuser(username)
        return res.get("value")
# webvalidateuser For showing Public URL End -


# -----------webgettemplatebatchName For showing Public URL Start +
@app.route('/webgettemplatebatchname',methods=['GET','POST'])
def webgettemplatebatchname():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        username = input_json.get("UserID")
        #password = input_json.get("password")
        res = gettemplatebatchname(username)
        return res.get("value")
# webgettemplatebatchName For showing Public URL End -
# -----------function name-sendReq Start +

# -----------webvalidatedocumentnofgmanufacturing For showing Public URL Start +
@app.route('/webvalidatedocumentnofgmanufacturing/<documentno>/<userid>',methods=['GET','POST'])
def webvalidatedocumentnofgmanufacturing(documentno,userid):
    res = validatedocumentnofgmanufacturing(documentno,userid)
    return res
# webvalidatedocumentnofgmanufacturing For showing Public URL End -

# -----------webvalidatemanuserialno For showing Public URL Start +
@app.route('/webvalidatemanuserialno/<srno>',methods=['GET','POST'])
def webvalidatemanuserialno(srno):
    res = validatemanuserialno(srno)
    return res
# webvalidatemanuserialno For showing Public URL End -




# -----------WebFGUpdateTransferOrderQty For showing Public URL Start +
@app.route('/webfgupdatetransferorderqty/<srno>/<uid>',methods=['GET','POST'])
def webfgupdatetransferorderqty(srno,uid):
    res = fgupdatetransferorderqty(srno,uid)
    return res
# WebFGUpdateTransferOrderQty For showing Public URL End -

# -----------ValidateSalesOrder For showing Public URL Start +
@app.route('/webvalidatesalesorder',methods=['GET','POST'])
def webvalidatesalesorder():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        username = input_json.get("OrderNo")
        res = validatesalesorder(username)
        return res.get("value")
# ValidateSalesOrder For showing Public URL End -


#**************************************************************************

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
# function name-sendReq Start -

# -----------function name-webuserlogin Start +



def webuserlogin(user_name,pass_word,login_type):
    print(user_name,pass_word,login_type)
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetWebUserBCPL?Company=Bodycare"

    req = "\"UserID\":\"user_name\",\"Password\":\"pass_word\",\"LoginType\":\"login_type\""
    
    req = req.replace("user_name", user_name)
    req = req.replace("pass_word", pass_word)
    req = req.replace("login_type", login_type)

    req = "{"+req+"}"
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
# function name-webuserlogin END -

# -----------function name-credentialsvalidate Start +
def credentialsvalidate(user_name,pass_word):
    print(user_name,pass_word)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_CredentialsValidate?Company=Bodycare"

    req = "\"UserID\":\"user_name\",\"UserPassword\":\"pass_word\""

    req = req.replace("user_name", user_name)
    req = req.replace("pass_word", pass_word)

    req = "{"+req+"}"
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
# function name-credentialsvalidate END -



# -----------function name-ItemListWS Start +
def itemlistws():
    url = "http://20.235.83.237:7048/BC200/ODataV4/Company('Bodycare')/ItemListWS"
    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, auth=HttpNtlmAuth(url+"VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    return response.json()
# function name-ItemListWS END -



# -----------function name-BarcodePrint Start +
def barcodeprint(phylotno,itemno,variantcode,printreport,uom,issuedtouid,no0fbarcodes,uommrp,pricegroupcode,purstndrdqty,createdby):
    #print(user_name,pass_word)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_BarcodePrint?Company=Bodycare"
    req = "\"PhyLotNo\":\"phylotno_\",\"ItemNo\":\"itemno_\",\"VariantCode\":\"variantcode_\",\"PrintReport\":\"printreport_\",\"UOM\":\"uom_\",\"IssuedToUID\":\"issuedtouid_\",\"No0fBarcodes\":\"no0fbarcodes_\",\"UOMMRP\":\"uommrp_\",\"PriceGroupCode\":\"pricegroupcode\",\"PurStndrdQty\":\"purstndrdqty_\",\"CreatedBy\":\"createdby_\""

    req = req.replace("phylotno_", phylotno)
    req = req.replace("itemno_", itemno)
    req = req.replace("variantcode_", variantcode)
    req = req.replace("printreport_", printreport)
    req = req.replace("uom_", uom)
    req = req.replace("issuedtouid_", issuedtouid)
    req = req.replace("no0fbarcodes_", no0fbarcodes)
    req = req.replace("uommrp_", uommrp)
    req = req.replace("pricegroupcode_", pricegroupcode)
    req = req.replace("purstndrdqty_", purstndrdqty)
    req = req.replace("createdby_", createdby)
    req = "{"+req+"}"
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
# function name-BarcodePrint END -



# -----------function name-credentialsvalidate Start +
def validateuser(user_name):
    #print(user_name)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateUser?Company=Bodycare"
    req = "\"UserID\":\"user_name\""

    req = req.replace("user_name", user_name)

    req = "{"+req+"}"
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
# function name-validateuser END -



# -----------function name-gettemplatebatchName Start +
def gettemplatebatchname(user_name):
    #print(user_name)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_GetTemplateBatchName?Company=Bodycare"

    req = "\"UserID\":\"user_name\""

    req = req.replace("user_name", user_name)

    req = "{"+req+"}"
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
# function name-gettemplatebatchName END -



# -----------function name-validatedocumentnofgmanufacturing Start +
def validatedocumentnofgmanufacturing(document_no,user_id):
    #print(user_name)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare"

    req = "\"DocumentNo\":\"documentno\",\"UserID\":\"userid\""

    req = req.replace("documentno", document_no)
    req = req.replace("userid", user_id)

    req = "{"+req+"}"
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
# function name-validatedocumentnofgmanufacturing END -


# -----------function name-ValidateManuSerialNo Start +
def validatemanuserialno(srl_no):
    #print(user_name)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateManuSerialNo?Company=Bodycare"

    req = "\"Srlno\":\"Srlno_\""

    req = req.replace("Srlno_", srl_no)

    req = "{"+req+"}"
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
# function name-ValidateManuSerialNo END -


# -----------function name-FGUpdateTransferOrderQty Start +
def fgupdatetransferorderqty(srl_no,user_id):
    #print(user_name)
    url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_FGUpdateTransferOrderQty?Company=Bodycare"

    req ="\"Srlno\":\"Srlno_\",\"UserID\":\"user_\""
    req = req.replace("Srlno_", srl_no)
    req = req.replace("user_", user_id)

    req = "{"+req+"}"
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
# function name-FGUpdateTransferOrderQty END -



# -----------function name-ValidateSalesOrder Start +
def validatesalesorder(order_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=Bodycare%20Creations%20Ltd."

    req ="\"OrderNo\":\"orderno_\""
    req = req.replace("orderno_", order_no)

    req = "{"+req+"}"
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
# function name-ValidateSalesOrder END -





# -----------function name-ValidateCartonBarcode Start +
def validatecartonbarcode(carton_barcode_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCartonBarcode?Company=Bodycare%20Creations%20Ltd."

    req ="\"CartonBarcodeNO\":\"carton_barcode_no_\""
    req = req.replace("carton_barcode_no_", carton_barcode_no)

    req = "{"+req+"}"
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
# function name-ValidateCartonBarcode END -




app.config["DEBUG"] = True

# starting flask application
if __name__ == '__main__':
    app.run(debug=True, port=6262)
    #app.run(host='192.168.1.44', port=6262, debug=True)
