import requests
import json
from requests_ntlm import HttpNtlmAuth
from flask import Flask, jsonify, request, render_template, redirect, url_for
import logging
from datetime import date, datetime

# validateuser

logging.basicConfig(filename="logs/BCLog" + str(date.today()) + ".log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# setting up flask app
app = Flask(__name__, template_folder='templates')


# -----------checkBalance For showing Public URL Start +
@app.route('/checkBalance/<vendor_code>', methods=['GET', 'POST'])
def checkBalance(vendor_code):
    res = sendReq(vendor_code)
    return res


# checkBalance For showing Public URL Start -

# -----------weblogin For showing Public URL Start +
@app.route('/weblogin/<username>/<password>/<logintype>', methods=['GET', 'POST'])
def weblogin(username, password, logintype):
    res = webuserlogin(username, password, logintype)
    return res


# weblogin For showing Public URL End -

# -----------webcredentialsvalidate For showing Public URL Start +
#@app.route('/webcredentialsvalidate/<username>/<password>', methods=['GET', 'POST'])
@app.route('/webcredentialsvalidate', methods=['GET', 'POST'])
def webcredentialsvalidate():
    if request.method == 'POST':
        #res = credentialsvalidate(username, password)
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        company_code = input_json.get("CompanyCode")
        user_id = input_json.get("UserID")
        user_password = input_json.get("UserPassword")
        res = credentialsvalidate(company_code,user_id,user_password)
        #return res
    else:
        company_code = request.args.get("CompanyCode")
        user_id = request.args.get("UserID")
        user_password = request.args.get("UserPassword")
        print(user_id)
        logger.info(str(user_id))
        res = credentialsvalidate(company_code,user_id,user_password)

    #return jsonify(res)
    return res

# webcredentialsvalidate For showing Public URL End -


# -----------webitemListws For showing Public URL Start +
@app.route('/webitemlistws', methods=['GET', 'POST'])
def webitemlistws():
    arr=[]
    js={}
    res = itemlistws()
    for i in res:
        js["No"]= i["No"]
        js["Description"] = i["Description"]
        arr.append(js)
    return arr


# webitemlistws For showing Public URL End -


# -----------webbarcodeprint For showing Public URL Start +
@app.route('/webbarcodeprint', methods=['GET', 'POST'])
def webbarcodeprint():
    if request.method == 'POST':
        input_json = request.get_json()
        # print(input_json)
        company_code = input_json.get("CompanyCode")
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
        res = barcodeprint(company_code, phylotno, itemno, variantcode, printreport, uom, issuedtouid, no0fbarcodes, uommrp,
                           pricegroupcode, purstndrdqty, createdby)
        # return res
        # return res.get("value")
        return res


# webbarcodeprint For showing Public URL End -


# -----------webvalidateuser For showing Public URL Start +
@app.route('/webvalidateuser', methods=['GET', 'POST'])
def webvalidateuser():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        username = input_json.get("UserID")
        res = validateuser(company_code,username)
        # return res.get("value")
        return res


# webvalidateuser For showing Public URL End -


# -----------webgettemplatebatchName For showing Public URL Start +
#@app.route('/webgettemplatebatchname/<username>', methods=['GET', 'POST'])
@app.route('/webgettemplatebatchname', methods=['GET', 'POST'])
def webgettemplatebatchname():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        company_code = input_json.get("CompanyCode")
        user_id = input_json.get("UserID")
        res = gettemplatebatchname(company_code, user_id)
        return res
    else:
        company_code = request.args.get("CompanyCode")
        user_id = request.args.get("UserID")
        print(user_id)
        logger.info(str(user_id))
        res = gettemplatebatchname(company_code, user_id)


# webgettemplatebatchName For showing Public URL End -
# -----------function name-sendReq Start +

# -----------webvalidatedocumentnofgmanufacturing For showing Public URL Start +
@app.route('/webvalidatedocumentnofgmanufacturing', methods=['GET', 'POST'])
def webvalidatedocumentnofgmanufacturing():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        document_No = input_json.get("DocumentNo")
        from_Location = input_json.get("FromLocation")
        to_Location = input_json.get("ToLocation")

        res = validatedocumentnofgmanufacturing(company_code, document_No, from_Location,to_Location)
    return res

# webvalidatedocumentnofgmanufacturing For showing Public URL End -


# -----------VDocumentNoFGManufac For showing Public URL Start +
@app.route('/webvDocumentNoFGManufac', methods=['GET', 'POST'])
def webvDocumentNoFGManufac():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        document_No = input_json.get("DocumentNo")
        user_ID = input_json.get("UserID")


        res = vDocumentNoFGManufac(company_code, document_No, user_ID)
    return res

# VDocumentNoFGManufac For showing Public URL End -





# -----------webvalidatemanuserialno For showing Public URL Start +
#@app.route('/webvalidatemanuserialno/<srno>', methods=['GET', 'POST'])
@app.route('/webvalidatemanuserialno', methods=['GET', 'POST'])
def webvalidatemanuserialno():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        company_code = input_json.get("CompanyCode")
        srno = input_json.get("Srlno")
        res = validatemanuserialno(company_code,srno)
        return res
    else:
        company_code = request.args.get("CompanyCode")
        srno = request.args.get("Srlno")
        print(srno)
        logger.info(str(srno))
        res = validatemanuserialno(company_code,srno)
        return res


# webvalidatemanuserialno For showing Public URL End -


# -----------WebFGUpdateTransferOrderQty For showing Public URL Start +
#@app.route('/webfgupdatetransferorderqty/<srno>/<uid>', methods=['GET', 'POST'])
@app.route('/webfgupdatetransferorderqty', methods=['GET', 'POST'])
def webfgupdatetransferorderqty():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        company_code = input_json.get("CompanyCode")
        srno = input_json.get("Srlno")
        uid = input_json.get("UserID")
        res = fgupdatetransferorderqty(company_code, srno, uid)
        return res
    else:
        company_code = request.args.get("CompanyCode")
        srno = request.args.get("Srlno")
        uid = request.args.get("UserID")
        print(uid)
        logger.info(str(uid))
        res = fgupdatetransferorderqty(company_code, srno, uid)
        return res

# WebFGUpdateTransferOrderQty For showing Public URL End -


# -----------ValidateSalesOrder For showing Public URL Start +
@app.route('/webvalidatesalesorder', methods=['GET', 'POST'])
def webvalidatesalesorder():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        orderno = input_json.get("OrderNo")
        company_code = input_json.get("CompanyCode")
        res = validatesalesorder(company_code, orderno)
        # return res.get("value")
        return res


# ValidateSalesOrder For showing Public URL End -

# -----------ValidateCartonBarcode For showing Public URL Start +
@app.route('/webvalidatecartonbarcode', methods=['GET', 'POST'])
def webvalidatecartonbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        cartonbarcodeno = input_json.get("CartonBarcodeNO")
        res = validatecartonbarcode(company_code,cartonbarcodeno)
        # return res.get("value")
        return res


# ValidateCartonBarcode For showing Public URL End -


# -----------ValidateEndUser For showing Public URL Start +
@app.route('/webvalidateenduser', methods=['GET', 'POST'])
def webvalidateenduser():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        endcode = input_json.get("EndCode")
        userid = input_json.get("UserID")
        cartonbarcode = input_json.get("CartonBarcode")
        salesorder = input_json.get("SalesOrder")

        res = validateenduser(company_code, endcode, userid, cartonbarcode, salesorder)
        # return res.get("value")
        return res


# ValidateEndUser For showing Public URL End -


# -----------ValidatePBarcode For showing Public URL Start +
@app.route('/webvalidatepbarcode', methods=['GET', 'POST'])
def webvalidatepbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        parent_barcode = input_json.get("ParentBarcode")

        res = validatepbarcode(company_code, parent_barcode)
        # return res.get("value")
        return res


# ValidatePBarcode For showing Public URL End -


# -----------ValidateCBarcode For showing Public URL Start +
@app.route('/webvalidatecbarcode', methods=['GET', 'POST'])
def webvalidatecbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("Barcode")

        res = validatecbarcode(company_code, bar_code)
        # return res.get("value")
        return res


# ValidateCBarcode For showing Public URL End -


# -----------BarcodePacking For showing Public URL Start +
@app.route('/webbarcodepacking', methods=['GET', 'POST'])
def webbarcodepacking():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        parent_barcode = input_json.get("ParentBarcode")
        child_barcode = input_json.get("ChildBarcode")
        user_id = input_json.get("UserID")

        res = barcodepacking(company_code, parent_barcode, child_barcode, user_id)
        # return res.get("value")
        return res


# BarcodePacking For showing Public URL End -


# -----------ValidateDocumentNoProduction For showing Public URL Start +
@app.route('/webvalidatedocumentnoproduction', methods=['GET', 'POST'])
def webvalidatedocumentnoproduction():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserID")

        res = validatedocumentnoproduction(company_code, document_no, user_id)
        # return res.get("value")
        return res


# ValidateDocumentNoProduction For showing Public URL End -


# -----------ValidateSerialNo For showing Public URL Start +
@app.route('/webvalidateserialno', methods=['GET', 'POST'])
def webvalidateserialno():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        sr_no = input_json.get("Srlno")
        document_no = input_json.get("DocNo")

        res = validateserialno(company_code, sr_no, document_no)
        # return res.get("value")
        return res


# ValidateSerialNo For showing Public URL End -


# -----------ValidateDocBarcode For showing Public URL Start +
@app.route('/webvalidatedocbarcode', methods=['GET', 'POST'])
def webvalidatedocbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        doc_bar_code = input_json.get("DocBarcode")
        user_id = input_json.get("UserID")
        template_name = input_json.get("TemplateName")
        batch_name = input_json.get("BatchName")
        doc_no = input_json.get("DocNo")

        res = validatedocbarcode(company_code, doc_bar_code, user_id, template_name, batch_name, doc_no)
        # return res.get("value")
        return res


# ValidateDocBarcode For showing Public URL End -


# -----------ValidateDocBarcode For showing Public URL Start +
@app.route('/webvalidateupbarcode', methods=['GET', 'POST'])
def webvalidateupbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("Barcode")

        res = validateupbarcode(company_code, bar_code)
        # return res.get("value")
        return res


# ValidateDocBarcode For showing Public URL End -


# req ="\"Barcode\":\"bar_code_\",\"PBarcode\":\"p_bar_code_\",\"OrderNo\":\"order_no_\""

# -----------ValidateUCBarcode For showing Public URL Start +
@app.route('/webvalidateucbarcode', methods=['GET', 'POST'])
def webvalidateucbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("Barcode")
        pbar_code = input_json.get("PBarcode")
        order_no = input_json.get("OrderNo")

        res = validateucbarcode(company_code, bar_code, pbar_code, order_no)
        # return res.get("value")
        return res


# ValidateUCBarcode For showing Public URL End -


# -----------BarcodeUnPacking For showing Public URL Start +
@app.route('/webbarcodeunpacking', methods=['GET', 'POST'])
def webbarcodeunpacking():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("ChildBarcode")
        pbar_code = input_json.get("ParentBarcode")
        user_id = input_json.get("UserID")

        res = barcodeunpacking(company_code, bar_code, pbar_code, user_id)
        # return res.get("value")
        return res


# BarcodeUnPacking For showing Public URL End -


# -----------ValidateUserPurch For showing Public URL Start +
@app.route('/webvalidateuserpurch', methods=['GET', 'POST'])
def webvalidateuserpurch():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        user_id = input_json.get("UserID")

        res = validateuserpurch(company_code, user_id)
        # return res.get("value")
        return res


# ValidateUserPurch For showing Public URL End -


# -----------validatedocnopurch For showing Public URL Start +
@app.route('/webvalidatedocnopurch', methods=['GET', 'POST'])
def webvalidatedocnopurch():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserID")

        res = validatedocnopurch(company_code, document_no, user_id)
        # return res.get("value")
        return res


# validatedocnopurch For showing Public URL End -


# -----------RMPurchaseStockTake For showing Public URL Start +
@app.route('/webrmpurchasestocktake', methods=['GET', 'POST'])
def webrmpurchasestocktake():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        childd_Bacode = input_json.get("ChilddBacode")
        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserId")

        res = rmpurchasestocktake(company_code, childd_Bacode, document_no, user_id)
        # return res.get("value")
        return res


# RMPurchaseStockTake For showing Public URL End -


# -----------OnlineValidateLocation For showing Public URL Start +
@app.route('/webonlinevalidatelocation', methods=['GET', 'POST'])
def webonlinevalidatelocation():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        location_code = input_json.get("Location")
        # document_no = input_json.get("DocumentNo")
        # user_id = input_json.get("UserId")

        res = onlinevalidatelocation(company_code, location_code)
        # return res.get("value")
        return res


# OnlineValidateLocation For showing Public URL End -


# ----------- OnlineValidateTrnsfrShpBarcode For showing Public URL Start +
@app.route('/webonlinevalidatetrnsfrshpbarcode', methods=['GET', 'POST'])
def webonlinevalidatetrnsfrshpbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        barcode_code = input_json.get("Barcode")

        res = onlinevalidatetrnsfrshpbarcode(company_code, barcode_code)
        # return res.get("value")
        return res


# OnlineValidateTrnsfrShpBarcode For showing Public URL End -


# ----------- OnlineTransferShipmentLooseToFresh For showing Public URL Start +
@app.route('/webonlinetransfershipmentloosetofresh', methods=['GET', 'POST'])
def webonlinetransfershipmentloosetofresh():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        barcode_code = input_json.get("Barcode")
        transfer_order = input_json.get("TransferOrder")
        from_location = input_json.get("FromLocation")

        res = onlinetransfershipmentloosetofresh(company_code, barcode_code, transfer_order, from_location)
        # return res.get("value")
        return res


# OnlineTransferShipmentLooseToFresh For showing Public URL End -


# ----------- CreateTransferHeader For showing Public URL Start +
@app.route('/webcreatetransferheader', methods=['GET', 'POST'])
def webcreatetransferheader():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        transfer_order = input_json.get("TransferOrder")
        from_location = input_json.get("FromLocation")
        to_location = input_json.get("ToLocation")
        work_oder_no = input_json.get("WorkOderNo")
        user_id = input_json.get("UserID")

        res = createtransferheader(transfer_order, from_location, to_location, work_oder_no, user_id)
        # return res.get("value")
        return res


# CreateTransferHeader For showing Public URL End -


# ----------- OnlineTransferShipment For showing Public URL Start +
@app.route('/webonlinetransfershipment', methods=['GET', 'POST'])
def webonlinetransfershipment():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("Barcode")
        transfer_order = input_json.get("TransferOrder")
        to_location = input_json.get("ToLocation")
        from_location = input_json.get("FromLocation")

        res = onlinetransfershipment(company_code, bar_code, transfer_order, to_location, from_location)
        # return res.get("value")
        return res


# OnlineTransferShipment For showing Public URL End -


# ----------- ValidateDocumentNo For showing Public URL Start +
@app.route('/webvalidatedocumentno', methods=['GET', 'POST'])
def webvalidatedocumentno():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        document_no = input_json.get("DocumentNo")
        u_id = input_json.get("UID")

        res = validatedocumentno(document_no, u_id)
        # return res.get("value")
        return res


# ValidateDocumentNo For showing Public URL End -


# ----------- ValidateArticalBarcode For showing Public URL Start +
@app.route('/webvalidatearticalbarcode', methods=['GET', 'POST'])
def webvalidatearticalbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        srl_no = input_json.get("Srlno")
        doc_no = input_json.get("DocNo")

        res = validatearticalbarcode(company_code, srl_no, doc_no)
        # return res.get("value")
        return res


# ValidateArticalBarcode For showing Public URL End -


# ----------- PCSStockTake For showing Public URL Start +
@app.route('/webpssstocktake', methods=['GET', 'POST'])
def webpssstocktake():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        srl_no = input_json.get("Srlno")
        doc_no = input_json.get("DocumentNo")
        u_id = input_json.get("UID")

        res = pssstocktake(company_code, srl_no, doc_no, u_id)
        # return res.get("value")
        return res


# PCSStockTake For showing Public URL End -


# ----------- ValidateReturnOrder For showing Public URL Start +
@app.route('/webvalidatereturnorder', methods=['GET', 'POST'])
def webvalidatereturnorder():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        return_order_no = input_json.get("ReturnOrderNo")

        res = validatereturnorder(company_code,return_order_no)
        # return res.get("value")
        return res


# ValidateReturnOrder For showing Public URL End -


# ----------- ValidateReturnBarcode For showing Public URL Start +
@app.route('/webvalidatereturnbarcode', methods=['GET', 'POST'])
def webvalidatereturnbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        rtrn_Barcode = input_json.get("RtrnBarcode")
        rtrnOrder_No = input_json.get("RtrnOrderNo")

        res = validatereturnbarcode(company_code, rtrn_Barcode,rtrnOrder_No)
        # return res.get("value")
        return res


# ValidateReturnBarcode For showing Public URL End -


# ----------- GoodsReturn For showing Public URL Start +
@app.route('/webgoodsreturn', methods=['GET', 'POST'])
def webgoodsreturn():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("RtrnBarcode")
        return_order_no = input_json.get("RtrnOrderNo")

        res = goodsreturn(company_code,bar_code,return_order_no)
        # return res.get("value")
        return res


# GoodsReturn For showing Public URL End -


# ******************************************** DistibutorPortal ++++++++++++++++

# ----------- ValidateWebUser For showing Public URL Start +
@app.route('/webvalidatewebuserdp', methods=['GET', 'POST'])
def webvalidatewebuserdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))


        user_id = input_json.get("UserID")
        p_w_s = input_json.get("PWS")
        login_type = input_json.get("LoginType")

        res = validatewebuserdp(user_id, p_w_s, login_type)
        # return res.get("value")
        return res
    else:
        user_id = request.args.get("UserID")
        p_w_s = request.args.get("PWS")
        login_type = request.args.get("LoginType")
        logger.info(str(user_id))

        res = validatewebuserdp(user_id, p_w_s, login_type)
        # return res.get("value")
        return res


# ----------- ValidateWebUser For showing Public URL End -



# ----------- ValidatewebuserdpWindow For showing Public URL End +
@app.route('/webvalidatewebuserdpWindow', methods=['GET', 'POST'])
def webvalidatewebuserdpWindow():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))

        company_code = input_json.get("CompanyCode")
        user_id = input_json.get("UserID")
        p_w_s = input_json.get("PWS")
        login_type = input_json.get("LoginType")

        res = validatewebuserdpWin(company_code, user_id, p_w_s, login_type)
        # return res.get("value")
        return res
    else:
        company_code = request.args.get("CompanyCode")
        user_id = request.args.get("UserID")
        p_w_s = request.args.get("PWS")
        login_type = request.args.get("LoginType")
        logger.info(str(user_id))

        res = validatewebuserdpWin(company_code,user_id, p_w_s, login_type)
        # return res.get("value")
        return res

# ----------- ValidatewebuserdpWindow For showing Public URL End -




# ----------- ValidateWebCustomer For showing Public URL Start +
@app.route('/webvalidatewebcustomerdp', methods=['GET', 'POST'])
def webvalidatewebcustomerdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        customer_code = input_json.get("CustomerCode")
        res = validatewebcustomerdp(customer_code)
        # return res.get("value")
        return res
    else:
        customer_code = request.args.get("CustomerCode")
        res = validatewebcustomerdp(customer_code)
        # return res.get("value")
        return res


# ----------- ValidateWebCustomer For showing Public URL End -


# ----------- ValidateWebCustomerWindow For showing Public URL Start +
@app.route('/webvalidatewebcustomerdpWin', methods=['GET', 'POST'])
def webvalidatewebcustomerdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        customer_code = input_json.get("CustomerCode")
        res = validatewebcustomerdpWin(company_code,customer_code)
        # return res.get("value")
        return res
    else:
        company_code = request.args.get("CompanyCode")
        customer_code = request.args.get("CustomerCode")
        res = validatewebcustomerdpWin(company_code,customer_code)
        # return res.get("value")
        return res


# ----------- ValidateWebCustomerWindow For showing Public URL End -



# ----------- WebUserExport For showing Public URL Start +
@app.route('/webwebuserexportdp', methods=['GET', 'POST'])
def webwebuserexportdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        user_id = input_json.get("UserID")

        res = webuserexport(user_id)
        # return res.get("value")
        return res
    else:
        user_id = request.args.get("UserID")
        res = webuserexport(user_id)
        # return res.get("value")
        print(res, "Response")
        return res


# ----------- WebUserExport For showing Public URL End -


# ----------- WebUserExportWindow For showing Public URL Start +
@app.route('/webwebuserexportdpWin', methods=['GET', 'POST'])
def webwebuserexportdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        user_id = input_json.get("UserID")

        res = webuserexportWin(company_code,user_id)
        # return res.get("value")
        return res
    else:
        company_code =  request.args.get("CompanyCode")
        user_id = request.args.get("UserID")
        res = webuserexportWin(company_code, user_id)
        # return res.get("value")
        print(res, "Response")
        return res


# ----------- WebUserExportWindow For showing Public URL End -




# ----------- ItemCategoryExport For showing Public URL Start +
@app.route('/webitemcategoryexportdp', methods=['GET', 'POST'])
def webitemcategoryexportdp():
    res = itemcategoryexport()
    # return res.get("value")
    return res
# ----------- ItemCategoryExport For showing Public URL End -



# ----------- ItemCategoryExportWindow For showing Public URL Start +
@app.route('/webitemcategoryexportdpWin', methods=['GET', 'POST'])
def webitemcategoryexportdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        res = itemcategoryexportWin(company_code)
        return res
    else:
        company_code = request.args.get("CompanyCode")
        res = itemcategoryexportWin(company_code)
        return res


# ----------- ItemCategoryExportWindow For showing Public URL End -




# ----------- OrderCategoryExport For showing Public URL Start +
@app.route('/webordercategoryexportdp', methods=['GET', 'POST'])
def webordercategoryexportdp():
    res = orderCategoryExport()
    # return res.get("value")
    return res
# ----------- OrderCategoryExport For showing Public URL End -


# ----------- OrderCategoryExportWindow For showing Public URL Start +
@app.route('/webordercategoryexportdpWin', methods=['GET', 'POST'])
def webordercategoryexportdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        company_code = input_json.get("CompanyCode")
        res = orderCategoryExportWin(company_code)
        # return res.get("value")
        return res
    else:
        company_code = request.args.get("CompanyCode")
        res = orderCategoryExportWin(company_code)
        print(res, "Response")
        return res

# ----------- OrderCategoryExportWindow For showing Public URL End -





# ----------- GetItemCategoryDetail For showing Public URL Start +
@app.route('/webgetitemcategorydetaildp', methods=['GET', 'POST'])
def webgetitemcategorydetaildp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_category_code = input_json.get("ItemCategoryCode")

        res = getitemcategorydetail(item_category_code)
        # return res.get("value")
        return res


# ----------- GetItemCategoryDetail For showing Public URL End -

# ----------- GetItemCategoryUOM For showing Public URL Start +
@app.route('/webgetitemcategoryuomdp', methods=['GET', 'POST'])
def webgetitemcategoryuomdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_category_code = input_json.get("ItemCategoryCode")

        res = getitemcategoryuom(item_category_code)
        # return res.get("value")
        return res


# ----------- GetItemCategoryUOM For showing Public URL End -


# ----------- GetNewNoSeriesOnlineSO For showing Public URL Start +
@app.route('/webgetnewnoseriesonlinesodp', methods=['GET', 'POST'])
def webgetnewnoseriesonlinesodp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        no_series_code = input_json.get("NoSeriesCode")

        res = getnewnoseriesonlineso(no_series_code)
        # return res.get("value")
        return res

# ----------- GetNewNoSeriesOnlineSO For showing Public URL End -



# ----------- GetNewNoSeriesOnlineSOWindow For showing Public URL Start +
@app.route('/webgetnewnoseriesonlinesodpWin', methods=['GET', 'POST'])
def webgetnewnoseriesonlinesodpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        no_series_code = input_json.get("NoSeriesCode")

        res = getnewnoseriesonlinesoWin(company_code,no_series_code)
        # return res.get("value")
        return res

# ----------- GetNewNoSeriesOnlineSOWindow For showing Public URL End -



# ----------- ItemExportLike For showing Public URL Start +
@app.route('/webitemexportlikedp', methods=['GET', 'POST'])
def webitemexportlikedp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_categ = input_json.get("ItemCateg")
        item_code = input_json.get("ItemCode")

        res = itemexportlike(item_categ,item_code)
        # return res.get("value")
        return res
# ----------- ItemExportLike For showing Public URL End -


# ----------- ValidateItem For showing Public URL Start +
@app.route('/webValidateItemdp', methods=['GET', 'POST'])
def webValidateItemdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_categ = input_json.get("ItemCategory")
        item_code = input_json.get("ItemCode")

        res = validateItem(item_categ,item_code)
        # return res.get("value")
        return res
# ----------- ValidateItem For showing Public URL End -



# ----------- ValidateItemWindow For showing Public URL Start +
@app.route('/webValidateItemdpWin', methods=['GET', 'POST'])
def webValidateItemdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        item_categ = input_json.get("ItemCategory")
        item_code = input_json.get("ItemCode")

        res = validateItemWin(company_code,item_categ,item_code)
        # return res.get("value")
        return res
# ----------- ValidateItemWindow For showing Public URL End -



# ----------- ValidateItemVariant For showing Public URL Start +
@app.route('/webvalidateItemVariantdp', methods=['GET', 'POST'])
def webvalidateItemVariantdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_code = input_json.get("ItemCode")
        item_Variant_Code = input_json.get("ItemVariantCode")

        res = validateItemVariant(item_code,item_Variant_Code)
        # return res.get("value")
        return res
# ----------- ValidateItemVariant For showing Public URL End -


# ----------- ValidateItemVariantWindow For showing Public URL Start +
@app.route('/webvalidateItemVariantdpWin', methods=['GET', 'POST'])
def webvalidateItemVariantdpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        item_code = input_json.get("ItemCode")
        item_Variant_Code = input_json.get("ItemVariantCode")

        res = validateItemVariantWin(company_code, item_code,item_Variant_Code)
        # return res.get("value")
        return res
# ----------- ValidateItemVariantWindow For showing Public URL End -



# ----------- UpdateUserIDInSaleOrderExport For showing Public URL Start +
@app.route('/webUpdateUserIDInSaleOrderExportdp', methods=['GET', 'POST'])
def webUpdateUserIDInSaleOrderExportdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        User_ID = input_json.get("UserID")
        docuent_No = input_json.get("DocuentNo")

        res = updateUserIDInSaleOrderExport(User_ID,docuent_No)
        # return res.get("value")
        return res
# ----------- UpdateUserIDInSaleOrderExport For showing Public URL End -



# ----------- ValidateItemNo For showing Public URL Start +
@app.route('/webValidateItemNodp', methods=['GET', 'POST'])
def webValidateItemNodp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        item_Code = input_json.get("ItemCode")


        res = validateItemNo(item_Code)
        # return res.get("value")
        return res
# ----------- ValidateItemNo For showing Public URL End -



# ----------- ValidateItemNoWindow For showing Public URL Start +
@app.route('/webValidateItemNodpWin', methods=['GET', 'POST'])
def webValidateItemNodpWin():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        item_Code = input_json.get("ItemCode")


        res = validateItemNoWin(company_code,item_Code)
        # return res.get("value")
        return res
# ----------- ValidateItemNoWindow For showing Public URL End -



# ----------- TransferLnArticalBarcode For showing Public URL Start +
@app.route('/webTransferLnArticalBarcodedp', methods=['GET', 'POST'])
def webTransferLnArticalBarcodedp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        company_code = input_json.get("CompanyCode")
        bar_code = input_json.get("Barcode")
        transfer_Order = input_json.get("TransferOrder")
        to_Location = input_json.get("ToLocation")
        from_Location = input_json.get("FromLocation")


        res = transferLnArticalBarcode(company_code,bar_code,transfer_Order,to_Location,from_Location)
        # return res.get("value")
        return res
# ----------- TransferLnArticalBarcode For showing Public URL End -

# ----------- itemexport For showing Public URL Start +
@app.route('/webitemexportdp', methods=['GET', 'POST'])
def webitemexportdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        no = input_json.get("No")
        description = input_json.get("Description")

        res = itemexport(no, description)
        # return res.get("value")
        return res


# ----------- itemexport For showing Public URL End -


# ----------- SaleOrderExportAPI For showing Public URL Start +
@app.route('/websaleorderexportapidp', methods=['GET', 'POST'])
def websaleorderexportapidp():
    if request.method == 'POST':
        input_json = request.get_json()
        input_json = input_json.get("message")
        print(type(input_json))
        input_json = json.loads(input_json)
        print(type(input_json))
        document_No = input_json.get("documentNo")
        customer_no = input_json.get("customerNo")
        item_no = input_json.get("itemNo")
        s_75 = input_json.get("s75")
        s_80S = input_json.get("s80S")
        s_85M = input_json.get("s85M")
        s_90L = input_json.get("s90L")
        s_95XL = input_json.get("s95XL")
        s_1002XL = input_json.get("s1002XL")
        s_1053XL = input_json.get("s1053XL")
        s_1104XL = input_json.get("s1104XL")
        s_1155XL = input_json.get("s1155XL")
        order_Type = input_json.get("orderType")
        selectOrder_Type = input_json.get("selectOrderType")
        item_Category_Code = input_json.get("itemCategoryCode")
        remark = input_json.get("remark")
        print(input_json, "*************")
        res = saleorderexportapi(document_No,customer_no,item_no,s_75,s_80S,s_85M,s_90L,s_95XL,s_1002XL,s_1053XL,s_1104XL,s_1155XL,order_Type,selectOrder_Type,item_Category_Code,remark)
        # return res.get("value")
        return res
    else:
        document_No = request.args.get("documentNo")
        customer_no = request.args.get("customerNo")
        item_no = request.args.get("itemNo")
        s_75 = request.args.get("s75")
        s_80S = request.args.get("s80S")
        s_85M = request.args.get("s85M")
        s_90L = request.args.get("s90L")
        s_95XL = request.args.get("s95XL")
        s_1002XL = request.args.get("s1002XL")
        s_1053XL = request.args.get("s1053XL")
        s_1104XL = request.args.get("s1104XL")
        s_1155XL = request.args.get("s1155XL")
        order_Type = request.args.get("orderType")
        selectOrder_Type = request.args.get("selectOrderType")
        item_Category_Code = request.args.get("itemCategoryCode")
        remark = request.args.get("remark")

        res = saleorderexportapi(document_No,customer_no, item_no, s_75, s_80S, s_85M, s_90L, s_95XL, s_1002XL, s_1053XL,
                                 s_1104XL, s_1155XL, order_Type, selectOrder_Type, item_Category_Code, remark)
        # return res.get("value")
        return res
# ----------- SaleOrderExportAPI For showing Public URL End -


# ----------- GetMailIDLoginUser For showing Public URL Start +
@app.route('/webgetMailIDLoginUserdp', methods=['GET', 'POST'])
def webgetMailIDLoginUserdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        user_id = input_json.get("UserID")

        res = getMailIDLoginUser(user_id)
        # return res.get("value")
        return res
    else:
        user_id = request.args.get("UserID")
        res = getMailIDLoginUser(user_id)
        # return res.get("value")
        print(res, "Response")
        return res


# ----------- GetMailIDLoginUser For showing Public URL End -



# ******************************** Mobile App Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +

# ----------- ItemCategoryApp For showing Public URL Start +
@app.route('/webitemcategoryapp', methods=['GET', 'POST'])
def webitemcategoryapp():
    res = itemcategoryapp()
    # return res.get("value")
    return res


# ----------- ItemCategoryApp For showing Public URL End -


# ----------- ItemMasterApp For showing Public URL Start +
@app.route('/webitemmasterapp', methods=['GET', 'POST'])
def webitemmasterapp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        catagory_code = input_json.get("catagory_code")
        res = itemmasterapp(catagory_code)
    else:
        catagory_code = request.args.get("catagory_code")
        print(catagory_code)
        logger.info(str(catagory_code))
        res = itemmasterapp(catagory_code)

    # return res.get("value")
    return jsonify(res)
# ----------- ItemMasterApp For showing Public URL End -

# ----------- ItemExportMobileAPI For showing Public URL Start +
@app.route('/webItemExportMobileAPI', methods=['GET', 'POST'])
def webItemExportMobileAPI():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        catagory_code = input_json.get("CategoryCode")
        res = itemExportMobileAPI(catagory_code)
    else:
        catagory_code = request.args.get("CategoryCode")
        print(catagory_code)
        logger.info(str(catagory_code))
        res = itemExportMobileAPI(catagory_code)

    # return res.get("value")
    return jsonify(res)
# ----------- ItemExportMobileAPI For showing Public URL End -



# ----------- CreateSOMobileApp For showing Public URL Start +
@app.route('/webCreateSOMobileApp', methods=['GET', 'POST'])
def webCreateSOMobileApp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))
        customer_No = input_json.get("CustomerNo")
        item_No = input_json.get("ItemNo")
        item_Size = input_json.get("ItemSize")
        item_Category_Code = input_json.get("ItemCategoryCode")
        remark = input_json.get("Remark")
        document_No = input_json.get("DocumentNo")
        bill_To_Customer = input_json.get("BillToCustomer")
        sell_To_Customer = input_json.get("SellToCustomer")
        user_ID = input_json.get("UserID")
        store_Name = input_json.get("StoreName")
        location_Code = input_json.get("LocationCode")
        res = createSOMobileApp(customer_No,item_No,item_Size,item_Category_Code,remark,document_No,bill_To_Customer,sell_To_Customer,user_ID,store_Name,location_Code)
    else:
        customer_No = request.args.get("CustomerNo")
        item_No = request.args.get("ItemNo")
        item_Size = request.args.get("ItemSize")
        item_Category_Code = request.args.get("ItemCategoryCode")
        remark = request.args.get("Remark")
        document_No = request.args.get("DocumentNo")
        bill_To_Customer = request.args.get("BillToCustomer")
        sell_To_Customer = request.args.get("SellToCustomer")
        user_ID = request.args.get("UserID")
        store_Name = request.args.get("StoreName")
        location_Code = request.args.get("LocationCode")

        print(customer_No)
        logger.info(str(customer_No))
        res = createSOMobileApp(customer_No, item_No, item_Size, item_Category_Code, remark, document_No,
                                bill_To_Customer, sell_To_Customer, user_ID, store_Name, location_Code)

    # return res.get("value")

    return jsonify(res)

# ----------- CreateSOMobileApp For showing Public URL End -




# ******************************** Mobile App End ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -


# ******************************************** DistibutorPortal -----------------


# *****************************************************************************************************************************


def sendReq(vendorcode):
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetVendorBalance?Company=Bodycare"
    # url = "http://20.235.83.237:8049/BodycareLive/ODataV4/GetVendorBalance_CredentialsValidate?Company=Bodycare%20Creations%20Ltd.

    req = "\"VendorCode\":\"{vendor_code}\""
    req = req.format(vendor_code=vendorcode)
    req = "{" + req + "}"

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    print(response.status_code)
    print(response.request.body)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-sendReq Start -

# -----------function name-webuserlogin Start +


def webuserlogin(user_name, pass_word, login_type):
    print(user_name, pass_word, login_type)
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetWebUserBCPL?Company=Bodycare"

    req = "\"UserID\":\"user_name\",\"Password\":\"pass_word\",\"LoginType\":\"login_type\""

    req = req.replace("user_name", user_name)
    req = req.replace("pass_word", pass_word)
    req = req.replace("login_type", login_type)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-webuserlogin END -

# -----------function name-credentialsvalidate Start +
def credentialsvalidate(comp_code, user_name, pass_word):
    print(user_name, pass_word)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_CredentialsValidate?Company=Bodycare"
    if comp_code == "BCPL":
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_CredentialsValidate?Company=Bodycare%20Creations%20Ltd.";
    else:
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_CredentialsValidate?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD";

    req = "\"UserID\":\"user_name\",\"UserPassword\":\"pass_word\""

    req = req.replace("user_name", user_name)
    req = req.replace("pass_word", pass_word)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    outputdata = str(outputdata)
    outputdata = outputdata.replace('\\\\','')
    return outputdata


# function name-credentialsvalidate END -


# -----------function name-ItemListWS Start +
def itemlistws():
    #url = "http://20.235.83.237:7048/BC200/ODataV4/Company('Bodycare')/ItemListWS"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/ItemListWebApp"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ItemListWS END -


url = "http://20.235.83.237:8049/BodycareLive/ODataV4/PrintBarcode_BarcodePrint?Company=Bodycare%20Creations%20Ltd.";


# -----------function name-BarcodePrint Start +
def barcodeprint(comp_code, phylotno, itemno, variantcode, printreport, uom, issuedtouid, no0fbarcodes, uommrp, pricegroupcode,
                 purstndrdqty, createdby):
    # print(user_name,pass_word)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_BarcodePrint?Company=Bodycare"
    if comp_code == "BCPL":
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/PrintBarcode_BarcodePrint?Company=Bodycare%20Creations%20Ltd.";
    else:
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/PrintBarcode_BarcodePrint?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD";

    req = "\"CompanyCode\":\"comp_code_\",\"PhyLotNo\":\"phylotno_\",\"ItemNo\":\"itemno_\",\"VariantCode\":\"variantcode_\",\"PrintReport\":\"printreport_\",\"UOM\":\"uom_\",\"IssuedToUID\":\"issuedtouid_\",\"No0fBarcodes\":\"no0fbarcodes_\",\"UOMMRP\":\"uommrp_\",\"PriceGroupCode\":\"pricegroupcode_\",\"PurStndrdQty\":\"purstndrdqty_\",\"CreatedBy\":\"createdby_\""
    # req = "\"UserID\":\"user_name\",\"UserPassword\":\"pass_word\""

    req = req.replace("comp_code_", comp_code)
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
    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-BarcodePrint END -

# -----------function name-credentialsvalidate Start +
def validateuser(company_code,user_name):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateUser?Company=Bodycare"
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUser?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUser?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"UserID\":\"user_name\""

    req = req.replace("user_name", user_name)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-validateuser END -


# -----------function name-gettemplatebatchName Start +
def gettemplatebatchname(company_code, user_name):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_GetTemplateBatchName?Company=Bodycare"
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GetTemplateBatchName?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GetTemplateBatchName?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"UserID\":\"user_name\""

    req = req.replace("user_name", user_name)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-gettemplatebatchName END -


# -----------function name-validatedocumentnofgmanufacturing Start +
def validatedocumentnofgmanufacturing(company_code, document_no, from_Location, to_Location):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare"
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoFGManufacturing?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"DocumentNo\":\"document_no_\",\"FromLocation\":\"from_Location_\",\"ToLocation\":\"to_Location_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("from_Location_", from_Location)
    req = req.replace("to_Location_", to_Location)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-validatedocumentnofgmanufacturing END -

# -----------function name-VDocumentNoFGManufac Start +
def vDocumentNoFGManufac(company_code, document_no, user_ID):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare"

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_VDocumentNoFGManufac?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_VDocumentNoFGManufac?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"DocumentNo\":\"document_no_\",\"UserID\":\"user_ID_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("user_ID_", user_ID)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-VDocumentNoFGManufac END -


# -----------function name-ValidateManuSerialNo Start +
def validatemanuserialno(company_code,srl_no):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateManuSerialNo?Company=Bodycare"

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateManuSerialNo?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateManuSerialNo?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"Srlno\":\"Srlno_\""

    req = req.replace("Srlno_", srl_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateManuSerialNo END -


# -----------function name-FGUpdateTransferOrderQty Start +
def fgupdatetransferorderqty(company_code, srl_no, user_id):
    # print(user_name)
    # url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_FGUpdateTransferOrderQty?Company=Bodycare"

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_FGUpdateTransferOrderQty?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_FGUpdateTransferOrderQty?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"Srlno\":\"Srlno_\",\"UserID\":\"user_\""
    req = req.replace("Srlno_", srl_no)
    req = req.replace("user_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-FGUpdateTransferOrderQty END -


# -----------function name-ValidateSalesOrder Start +
def validatesalesorder(company_code, order_no):
    #todo print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code ==None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"OrderNo\":\"orderno_\""
    req = req.replace("orderno_", order_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateSalesOrder END -


# -----------function name-ValidateCartonBarcode Start +
def validatecartonbarcode(company_code, carton_barcode_no):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCartonBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCartonBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"CartonBarcodeNO\":\"carton_barcode_no_\""
    req = req.replace("carton_barcode_no_", carton_barcode_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateCartonBarcode END -


# -----------function name-ValidateEndUser Start +
def validateenduser(company_code, end_code, user_id, carton_barcode, sales_order):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateEndUser?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateEndUser?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"EndCode\":\"EndCode_\",\"UserID\":\"user_id_\",\"CartonBarcode\":\"carton_barcode_\",\"SalesOrder\":\"sales_order_\""

    req = req.replace("EndCode_", end_code)
    req = req.replace("user_id_", user_id)
    req = req.replace("carton_barcode_", carton_barcode)
    req = req.replace("sales_order_", sales_order)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateEndUser END -


# -----------function name-ValidatePBarcode Start +
def validatepbarcode(company_code, parent_barcode):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidatePBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidatePBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ParentBarcode\":\"parent_barcode_\""

    req = req.replace("parent_barcode_", parent_barcode)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidatePBarcode END -


# -----------function name-ValidateCBarcode Start +
def validatecbarcode(company_code, Bar_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"Barcode\":\"Bar_code_\""

    req = req.replace("Bar_code_", Bar_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateCBarcode END -


# -----------function name-BarcodePacking Start +
def barcodepacking(company_code, parent_barcode, child_barcode, user_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_BarcodePacking?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ParentBarcode\":\"parent_barcode_\",\"ChildBarcode\":\"child_barcode_\",\"UserID\":\"user_id_\""

    req = req.replace("parent_barcode_", parent_barcode)
    req = req.replace("child_barcode_", child_barcode)
    req = req.replace("user_id_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-BarcodePacking END -


# -----------function name-ValidateDocumentNoProduction Start +
def validatedocumentnoproduction(company_code,document_no, user_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoProduction?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoProduction?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"DocumentNo\":\"document_no_\",\"UserID\":\"user_id_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("user_id_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateDocumentNoProduction END -


# -----------function name-ValidateSerialNo Start +
def validateserialno(company_code, barcodeserialno, document_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSerialNo?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSerialNo?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Srlno\":\"barcodeserialno_\",\"DocNo\":\"document_no_\""

    req = req.replace("barcodeserialno_", barcodeserialno)
    req = req.replace("document_no_", document_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateSerialNo END -


# -----------function name-ValidateDocBarcode Start +
def validatedocbarcode(company_code, doc_bar_code, user_id, template_name, batch_name, doc_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"DocBarcode\":\"doc_bar_code_\",\"UserID\":\"user_id_\",\"TemplateName\":\"template_name_\",\"BatchName\":\"batch_name_\",\"DocNo\":\"doc_no_\""

    req = req.replace("doc_bar_code_", doc_bar_code)
    req = req.replace("user_id_", user_id)
    req = req.replace("template_name_", template_name)
    req = req.replace("batch_name_", batch_name)
    req = req.replace("doc_no_", doc_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateDocBarcode END -


# -----------function name-ValidateUPBarcode Start +
def validateupbarcode(company_code, bar_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUPBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUPBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Barcode\":\"barcode_\""

    req = req.replace("barcode_", bar_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateUPBarcode END -


# -----------function name-ValidateUCBarcode Start +
def validateucbarcode(company_code, bar_code, pbcode, order_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUCBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUCBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Barcode\":\"bar_code_\",\"PBarcode\":\"pbcode_\",\"OrderNo\":\"order_no_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("pbcode_", pbcode)
    req = req.replace("order_no_", order_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateUCBarcode END -


# -----------function name-BarcodeUnPacking Start +
def barcodeunpacking(company_code, bar_code, pbcode, u_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_BarcodeUnPacking?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_BarcodeUnPacking?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ChildBarcode\":\"bar_code_\",\"ParentBarcode\":\"pbcode_\",\"UserID\":\"u_id_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("pbcode_", pbcode)
    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-BarcodeUnPacking END -


# -----------function name-ValidateUserPurch Start +
def validateuserpurch(company_code, u_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUserPurch?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUserPurch?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"UserID\":\"u_id_\""

    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateUserPurch END -


# -----------function name-ValidateDocNoPurch Start +
def validatedocnopurch(company_code, document_no, u_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocNoPurch?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocNoPurch?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"DocumentNo\":\"document_no_\",\"UserID\":\"u_id_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateDocNoPurch END -


# -----------function name-RMPurchaseStockTake Start +
def rmpurchasestocktake(company_code, ankit, document_no, u_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_RMPurchaseStockTake?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"ChilddBacode\":\"ankit_\",\"DocumentNo\":\"document_no_\",\"UserId\":\"u_id_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("ankit_", ankit)
    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-RMPurchaseStockTake END -


# -----------function name-OnlineValidateLocation Start +
def onlinevalidatelocation(company_code, location_Code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineValidateLocation?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Location\":\"location_Code_\""

    req = req.replace("location_Code_", location_Code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-OnlineValidateLocation END -


# -----------function name-OnlineValidateTrnsfrShpBarcode Start +
def onlinevalidatetrnsfrshpbarcode(company_code,bar_code):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineValidateTrnsfrShpBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineValidateTrnsfrShpBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"Barcode\":\"bar_code_\""

    req = req.replace("bar_code_", bar_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-OnlineValidateTrnsfrShpBarcode END -


# -----------function name-OnlineTransferShipmentLooseToFresh Start +
def onlinetransfershipmentloosetofresh(company_code, bar_code, transfer_order, from_location):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipmentLooseToFresh?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipmentLooseToFresh?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("transfer_order_", transfer_order)
    req = req.replace("from_location_", from_location)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-OnlineTransferShipmentLooseToFresh END -


# -----------function name-CreateTransferHeader Start +
def createtransferheader(transfer_order, from_location, to_location, work_oder_no, user_id):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_CreateTransferHeader?Company=Bodycare%20Creations%20Ltd."

    req = "\"TransferOrder\":\"transfer_order_\",\"FromLocation\":\"from_location_\",\"ToLocation\":\"to_location_\",\"WorkOderNo\":\"work_oder_no_\",\"UserID\":\"user_id_\""

    req = req.replace("transfer_order_", transfer_order)
    req = req.replace("from_location_", from_location)
    req = req.replace("to_location_", to_location)
    req = req.replace("work_oder_no_", work_oder_no)
    req = req.replace("user_id_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-CreateTransferHeader END -


# -----------function name-OnlineTransferShipment Start +
def onlinetransfershipment(company_code, bar_code, transfer_order, to_location, from_location):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipment?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipment?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"ToLocation\":\"to_location_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("transfer_order_", transfer_order)
    req = req.replace("to_location_", to_location)
    req = req.replace("from_location_", from_location)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-OnlineTransferShipment END -


# -----------function name-OnlineTransferShipment Start +
def onlinetransfershipment(bar_code, transfer_order, to_location, from_location):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipment?Company=Bodycare%20Creations%20Ltd."

    req = "\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"ToLocation\":\"to_location_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("transfer_order_", transfer_order)
    req = req.replace("to_location_", to_location)
    req = req.replace("from_location_", from_location)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-OnlineTransferShipment END -


# -----------function name-ValidateDocumentNo Start +
def validatedocumentno(document_no, u_id):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNo?Company=Bodycare%20Creations%20Ltd."

    req = "\"DocumentNo\":\"document_no_\",\"UID\":\"u_id_\""

    req = req.replace("document_no_", document_no)
    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateDocumentNo END -


# -----------function name-ValidateArticalBarcode Start +
def validatearticalbarcode(company_code,srl_no, doc_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateArticalBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateArticalBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"Srlno\":\"srl_no_\",\"DocNo\":\"doc_no_\""

    req = req.replace("srl_no_", srl_no)
    req = req.replace("doc_no_", doc_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateArticalBarcode END -


# -----------function name-PCSStockTake Start +
def pssstocktake(company_code, srl_no, doc_no, u_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_PCSStockTake?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_PCSStockTake?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"Srlno\":\"srl_no_\",\"DocumentNo\":\"doc_no_\",\"UID\":\"u_id_\""

    req = req.replace("srl_no_", srl_no)
    req = req.replace("doc_no_", doc_no)
    req = req.replace("u_id_", u_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-PCSStockTake END -


# -----------function name-ValidateReturnOrder Start +
def validatereturnorder(company_code, return_order_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateReturnOrder?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateReturnOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"ReturnOrderNo\":\"return_order_no_\""

    req = req.replace("return_order_no_", return_order_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateReturnOrder END -


# -----------function name-ValidateReturnBarcode Start +
def validatereturnbarcode(company_code, rtrn_barcode, rtrn_order_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateReturnBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSalesOrder?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"RtrnBarcode\":\"rtrn_barcode_\",\"RtrnOrderNo\":\"rtrn_order_no_\""

    req = req.replace("rtrn_barcode_", rtrn_barcode)
    req = req.replace("rtrn_order_no_", rtrn_order_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateReturnBarcode END -


# -----------function name-GoodsReturn Start +
def goodsreturn(company_code, rtrn_barcode, rtrn_order_no):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GoodsReturn?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GoodsReturn?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"RtrnBarcode\":\"rtrn_barcode_\",\"RtrnOrderNo\":\"rtrn_order_no_\""

    req = req.replace("rtrn_barcode_", rtrn_barcode)
    req = req.replace("rtrn_order_no_", rtrn_order_no)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-GoodsReturn END -


# *************************************************** DistibutorPortal Function ++++++++++++++++++++++++++++++++++++++++++++++

# -----------function name-ValidateWebUser Start +
def validatewebuserdp(user_id, p_w_s, login_type):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebUser?Company=Bodycare%20Creations%20Ltd."

    req = "\"UserID\":\"user_id_\",\"PWS\":\"p_w_s_\",\"LoginType\":\"login_type_\""

    req = req.replace("user_id_", user_id)
    req = req.replace("p_w_s_", p_w_s)
    req = req.replace("login_type_", login_type)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateWebUser END -


# -----------function name-ValidatewebuserdpWindow Start +
def validatewebuserdpWin(company_code,user_id, p_w_s, login_type):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebUser?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateWebUser?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"UserID\":\"user_id_\",\"PWS\":\"p_w_s_\",\"LoginType\":\"login_type_\""

    req = req.replace("user_id_", user_id)
    req = req.replace("p_w_s_", p_w_s)
    req = req.replace("login_type_", login_type)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidatewebuserdpWindow END -



# -----------function name-ValidateWebCustomer Start +
def validatewebcustomerdp(customer_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebCustomer?Company=Bodycare%20Creations%20Ltd."

    req = "\"CustomerCode\":\"customer_code_\""

    req = req.replace("customer_code_", customer_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateWebCustomer END -



# -----------function name-ValidateWebCustomerWindow Start +
def validatewebcustomerdpWin(company_code,customer_code):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebCustomer?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateWebCustomer?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"CustomerCode\":\"customer_code_\""

    req = req.replace("customer_code_", customer_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ValidateWebCustomerWindow END -




# -----------function name - WebUserExport Start +
def webuserexport(user_id):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_WebUserExport?Company=Bodycare%20Creations%20Ltd."

    req = "\"UserID\":\"user_id_\""

    req = req.replace("user_id_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-WebUserExport END -




# -----------function name - WebUserExportWindow Start +
def webuserexportWin(company_code,user_id):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_WebUserExport?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_WebUserExport?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = "\"UserID\":\"user_id_\""

    req = req.replace("user_id_", user_id)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-WebUserExportWindow END -



# -----------function name - ItemCategoryExport Start +
def itemcategoryexport():
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemCategoryExport?Company=Bodycare%20Creations%20Ltd."

    req = ""

    print(req)

    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# -----------function name - ItemCategoryExport Start -




# -----------function name - ItemCategoryExportWindow Start +
def itemcategoryexportWin(company_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemCategoryExport?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemCategoryExport?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = ""

    print(req)

    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# -----------function name - ItemCategoryExportWindow Start -





# -----------function name - OrderCategoryExport Start +
def orderCategoryExport():
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_OrderCategoryExport?Company=Bodycare%20Creations%20Ltd."

    req = ""

    print(req)

    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# -----------function name - OrderCategoryExport Start -



# -----------function name - OrderCategoryExportWindow Start +
def orderCategoryExportWin(company_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_OrderCategoryExport?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_OrderCategoryExport?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}



    req = ""

    print(req)

    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# -----------function name - OrderCategoryExportWindow Start -


# -----------function name - GetItemCategoryDetail Start +
def getitemcategorydetail(item_category_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetItemCategoryDetail?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCategoryCode\":\"item_category_code_\""

    req = req.replace("item_category_code_", item_category_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-GetItemCategoryDetail END -


# -----------function name - GetItemCategoryUOM Start +
def getitemcategoryuom(item_category_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetItemCategoryUOM?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCategoryCode\":\"item_category_code_\""

    req = req.replace("item_category_code_", item_category_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-GetItemCategoryUOM END -

# -----------function name - GetNewNoSeriesOnlineSO Start +
def getnewnoseriesonlineso(no_series_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetNewNoSeriesOnlineSO?Company=Bodycare%20Creations%20Ltd."

    req = "\"NoSeriesCode\":\"no_series_code_\""

    req = req.replace("no_series_code_", no_series_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-GetNewNoSeriesOnlineSO END -



# -----------function name - GetNewNoSeriesOnlineSOWindow Start +
def getnewnoseriesonlinesoWin(company_code,no_series_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetNewNoSeriesOnlineSO?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetNewNoSeriesOnlineSO?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"NoSeriesCode\":\"no_series_code_\""

    req = req.replace("no_series_code_", no_series_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-GetNewNoSeriesOnlineSOWindow END -




# -----------function name - ItemExportLike Start +
def itemexportlike(item_categ,item_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemExportLike?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCateg\":\"item_categ_\",\"ItemCode\":\"item_code_\""

    req = req.replace("item_categ_", item_categ)
    req = req.replace("item_code_", item_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ItemExportLike END -



# -----------function name - ValidateItem Start +
def validateItem(item_categ,item_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItem?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCategory\":\"item_category_\",\"ItemCode\":\"item_code_\""

    req = req.replace("item_category_", item_categ)
    req = req.replace("item_code_", item_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ValidateItem END -



# -----------function name - ValidateItemWindow Start +
def validateItemWin(company_code,item_categ,item_code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItem?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateItem?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ItemCategory\":\"item_category_\",\"ItemCode\":\"item_code_\""

    req = req.replace("item_category_", item_categ)
    req = req.replace("item_code_", item_code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ValidateItemWindow END -



# -----------function name - ValidateItemVariant Start +
def validateItemVariant(item_code,item_Variant_Code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItemVariant?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCode\":\"item_code_\",\"ItemVariantCode\":\"item_Variant_Code_\""

    req = req.replace("item_code_", item_code)
    req = req.replace("item_Variant_Code_", item_Variant_Code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ValidateItemVariant END -



# -----------function name - ValidateItemVariantWindow Start +
def validateItemVariantWin(company_code, item_code,item_Variant_Code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItemVariant?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateItemVariant?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"ItemCode\":\"item_code_\",\"ItemVariantCode\":\"item_Variant_Code_\""

    req = req.replace("item_code_", item_code)
    req = req.replace("item_Variant_Code_", item_Variant_Code)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ValidateItemVariantWindow END -



# -----------function name - UpdateUserIDInSaleOrderExport Start +
def updateUserIDInSaleOrderExport(user_ID,docuent_No):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_UpdateUserIDInSaleOrderExport?Company=Bodycare%20Creations%20Ltd."

    req = "\"UserID\":\"user_ID_\",\"DocuentNo\":\"docuent_No_\""

    req = req.replace("user_ID_", user_ID)
    req = req.replace("docuent_No_", docuent_No)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - UpdateUserIDInSaleOrderExport END -


# -----------function name - ValidateItemNoWindow Start +
def validateItemNo(item_Code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItemNo?Company=Bodycare%20Creations%20Ltd."

    req = "\"ItemCode\":\"item_Code_\""

    req = req.replace("item_Code_", item_Code)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - ValidateItemNoWindow END -



# -----------function name - ValidateItemNoWindow Start +
def validateItemNoWin(company_code, item_Code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItemNo?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateItemNo?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ItemCode\":\"item_Code_\""

    req = req.replace("item_Code_", item_Code)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - ValidateItemNoWindow END -



# -----------function name - ValidateItemNo Start +
def validateItemNo(company_code, item_Code):
    # print(user_name)
    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateItemNo?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateItemNo?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}

    req = "\"ItemCode\":\"item_Code_\""

    req = req.replace("item_Code_", item_Code)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - ValidateItemNo END -


# -----------function name - GetMailIDLoginUser Start +
def getMailIDLoginUser(user_ID):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_GetMailIDLoginUser?Company=Bodycare%20Creations%20Ltd."

    req = "\"UserID\":\"user_ID_\""

    req = req.replace("user_ID_", user_ID)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - GetMailIDLoginUser END -



# -----------function name - TransferLnArticalBarcode Start +
def transferLnArticalBarcode(company_code,bar_code,transfer_Order,to_Location,from_Location):
    # print(user_name)

    if (company_code == "BCPL"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_TransferLnArticalBarcode?Company=Bodycare%20Creations%20Ltd."
    elif (company_code == "ANU"):
        url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_TransferLnArticalBarcode?Company=ANUKAMPA%20EXPORTS%20PVT%20LTD"
    elif (company_code == "" or company_code == None):
        return {"id": "0", "Success": "False", "Message": "CompanyCode Node is missing"}
    else:
        return {"id": "0", "Success": "False", "Message": "Invalid Company Code"}


    req = "\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_Order_\",\"ToLocation\":\"to_Location_\",\"FromLocation\":\"from_Location_\""

    req = req.replace("bar_code_", bar_code)
    req = req.replace("transfer_Order_", transfer_Order)
    req = req.replace("to_Location_", to_Location)
    req = req.replace("from_Location_", from_Location)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - TransferLnArticalBarcode END -


# -----------function name - ItemExport Start +
def itemexport(no,description):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/ItemListWebApp"

    req = "\"No\":\"no_\",\"Description\":\"description_\""

    req = req.replace("no_", no)
    req = req.replace("description_", description)

    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name-ItemExport END -



# -----------function name - SaleOrderExportAPI Start +
def saleorderexportapi(document_No,customer_no,item_no,s_75,s_80S,s_85M,s_90L,s_95XL,s_1002XL,s_1053XL,s_1104XL,s_1155XL,order_Type, selectOrder_Type, item_Category_Code,remark):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/SaleOrderExportAPI"

    print(s_75,"hi")
    payload = json.dumps({
        "documentNo" : document_No,
        "customerNo": customer_no,
        "itemNo": item_no,
        "s75": float(s_75),
        "s80S": float(s_80S),
        "s85M": float(s_85M),
        "s90L": float(s_90L),
        "s95XL": float(s_95XL),
        "s1002XL": float(s_1002XL),
        "s1053XL": float(s_1053XL),
        "s1104XL": float(s_1104XL),
        "s1155XL": float(s_1155XL),
        "orderType": order_Type,
        "selectOrderType" :selectOrder_Type,
        "itemCategoryCode": item_Category_Code,
        "remark": remark
    })

    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text,response.status_code)
    outputdata = checkresponse(response.status_code, response.json())
    if(outputdata == True):
        return {"Message": "True"}
    return outputdata
# function name-SaleOrderExportAPI END -


# -----------function name - ItemCategoryApp Start +
def itemcategoryapp():
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemCategoryApp?Company=Bodycare%20Creations%20Ltd."

    req = ""

    print(req)

    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ItemCategoryApp END -

# -----------function name - ItemExportMobileAPI Start +
def itemExportMobileAPI(category_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemExportMobileAPI?Company=Bodycare%20Creations%20Ltd."

    req = "\"CategoryCode\":\"category_code_\""

    req = req.replace("category_code_", category_code)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))


    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())

    return outputdata

# function name - ItemExportMobileAPI END -



# ******************************** Mobile App Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +

# -----------function name - ItemMasterApp Start +
def itemmasterapp(item_category_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/ItemMasterApp"
    if (item_category_code == None or item_category_code == ""):
        url = url
    else:
        print("Not none")
        url = url + "?$filter=Catagory_Code%20eq%20%27" + item_category_code + "%27"

    req = ""
    payload = req

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata


# function name-ItemMasterApp END -



# -----------function name - CreateSOMobileApp Start +
def createSOMobileApp(customer_No,item_No,item_Size,item_Category_Code,remark,document_No,bill_To_Customer,sell_To_Customer,user_ID,store_Name,location_Code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/MobileAppCU_CreateSOMobileApp?Company=Bodycare%20Creations%20Ltd."

    #req = "\"CustomerNo\":\"customer_No_\",\"ItemNo\":\"item_No_\",\"ItemSize\":\"item_Size_\",\"ItemCategoryCode\":\"item_Category_Code_\",\"Remark\":\"remark_\",\"DocumentNo\":\"document_No_\",\"BillToCustomer\":\"bill_To_Customer_\",\"SellToCustomer\":\"sell_To_Customer_\",\"UserID\":\"user_ID_\",\"StoreName\":\"store_Name_\",\"LocationCode\":\"location_Code_\""
    req = "\"CustomerNo\":\"customer_No_\",\"ItemNo\":\"item_No_\",\"ItemSizeXS\":\"item_SizeXS_\",\"ItemSizeS\":\"item_SizeS_\",\"ItemSizeM\":\"item_SizeM_\",\"ItemSizeL\":\"item_SizeL_\",\"ItemSizeXL\":\"item_SizeXL_\",\"ItemSizeXXL\":\"item_SizeXXL_\",\"ItemSizeXXXL\":\"item_SizeXXXL_\",\"ItemCategoryCode\":\"item_Category_Code_\",\"Remark\":\"remark_\",\"DocumentNo\":\"document_No_\",\"BillToCustomer\":\"bill_To_Customer_\",\"SellToCustomer\":\"sell_To_Customer_\",\"UserID\":\"user_ID_\",\"StoreName\":\"store_Name_\",\"LocationCode\":\"location_Code_\""


    item_Size = item_Size.split(',')

    req = req.replace("customer_No_", customer_No)
    req = req.replace("item_No_", item_No)
    req = req.replace("item_SizeXS_", item_Size[0]) #1
    req = req.replace("item_SizeS_", item_Size[1]) #2
    req = req.replace("item_SizeM_", item_Size[2]) #3
    req = req.replace("item_SizeL_", item_Size[3]) #4
    req = req.replace("item_SizeXL_", item_Size[4]) #5
    req = req.replace("item_SizeXXL_", item_Size[5]) #6
    req = req.replace("item_SizeXXXL_", item_Size[6])  # 7
    req = req.replace("item_Category_Code_", item_Category_Code)
    req = req.replace("remark_", remark)
    req = req.replace("document_No_", document_No)
    req = req.replace("bill_To_Customer_", bill_To_Customer)
    req = req.replace("sell_To_Customer_", sell_To_Customer)
    req = req.replace("user_ID_", user_ID)
    req = req.replace("store_Name_", store_Name)
    req = req.replace("location_Code_", location_Code)


    req = "{" + req + "}"
    print(req)

    payload = json.dumps({
        "inputJson": req
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata

# function name - CreateSOMobileApp END -




# ******************************** Mobile App End ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -


# *************************************************** DistibutorPortal Function -----------------------------------------------------


def checkresponse(state_code, response):
    print("Ali-",state_code)
    #print("Firoj -", response)
    if (state_code == 200):
        return response.get("value")
    elif (state_code == 400):
        err_txt = response.get("error")
        try:
            if ("Application" in err_txt.get("code")):
                return {"Message": err_txt.get("message")}
        except Exception as e:
            return err_txt
    elif (state_code == 404):
        #return response.get("server not available")
        abc = response.get("error")
        Abcd = abc.get("message")
        WINDOWS_LINE_ENDING = b'\r\n'
        #without_line_breaks = Abcd.replace(WINDOWS_LINE_ENDING, "")
        data = {
            'Success': 'False',
            'Message': Abcd
        }
        dict_1 = json.dumps(data)  # converting dictionary to JSON
        #print(dict_1)  # {'Name' : 'Felix','Occupation' : 'Doctor'}
        return dict_1
    elif (state_code == 408):
        return response.get("request waiting timeout")
    elif (state_code == 201):
        if (response.get("@odata.etag") != None):
            return True
        else:
            return False


app.config["DEBUG"] = True

# starting flask application
if __name__ == '__main__':
    # app.run(debug=True, port=6262)
    #app.run(host='192.168.1.44', port=6262, debug=True)
    app.run(host='127.0.0.1', port=6262, debug=True)
