import requests
import json
from requests_ntlm import HttpNtlmAuth
from flask import Flask, jsonify, request, render_template, redirect, url_for
import logging
from datetime import date,datetime

#validateuser

logging.basicConfig(filename="logs/BCLog"+str(date.today())+".log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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
        #return res.get("value")
        return res
# webbarcodeprint For showing Public URL End -


# -----------webvalidateuser For showing Public URL Start +
@app.route('/webvalidateuser',methods=['GET','POST'])
def webvalidateuser():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        username = input_json.get("UserID")
        res = validateuser(username)
        #return res.get("value")
        return res


# webvalidateuser For showing Public URL End -



# -----------webgettemplatebatchName For showing Public URL Start +
@app.route('/webgettemplatebatchname/<username>',methods=['GET','POST'])
def webgettemplatebatchname(username):
    res = gettemplatebatchname(username)
    return res
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
        orderno = input_json.get("OrderNo")
        res = validatesalesorder(orderno)
        #return res.get("value")
        return res
# ValidateSalesOrder For showing Public URL End -

# -----------ValidateCartonBarcode For showing Public URL Start +
@app.route('/webvalidatecartonbarcode',methods=['GET','POST'])
def webvalidatecartonbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        cartonbarcodeno = input_json.get("CartonBarcodeNO")
        res = validatecartonbarcode(cartonbarcodeno)
        #return res.get("value")
        return res
# ValidateCartonBarcode For showing Public URL End -


# -----------ValidateEndUser For showing Public URL Start +
@app.route('/webvalidateenduser',methods=['GET','POST'])
def webvalidateenduser():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        endcode = input_json.get("EndCode")
        userid = input_json.get("UserID")
        cartonbarcode = input_json.get("CartonBarcode")
        salesorder = input_json.get("SalesOrder")
        
        res = validateenduser(endcode,userid,cartonbarcode,salesorder)
        #return res.get("value")
        return res
# ValidateEndUser For showing Public URL End -


# -----------ValidatePBarcode For showing Public URL Start +
@app.route('/webvalidatepbarcode',methods=['GET','POST'])
def webvalidatepbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        parent_barcode = input_json.get("ParentBarcode")
        
        res = validatepbarcode(parent_barcode)
        #return res.get("value")
        return res
# ValidatePBarcode For showing Public URL End -


# -----------ValidateCBarcode For showing Public URL Start +
@app.route('/webvalidatecbarcode',methods=['GET','POST'])
def webvalidatecbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        bar_code = input_json.get("Barcode")
        
        res = validatecbarcode(bar_code)
        #return res.get("value")
        return res
# ValidateCBarcode For showing Public URL End -


# -----------BarcodePacking For showing Public URL Start +
@app.route('/webbarcodepacking',methods=['GET','POST'])
def webbarcodepacking():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        parent_barcode = input_json.get("ParentBarcode")
        child_barcode = input_json.get("ChildBarcode")
        user_id = input_json.get("UserID")
        
        res = barcodepacking(parent_barcode,child_barcode,user_id)
        #return res.get("value")
        return res
# BarcodePacking For showing Public URL End -


# -----------ValidateDocumentNoProduction For showing Public URL Start +
@app.route('/webvalidatedocumentnoproduction',methods=['GET','POST'])
def webvalidatedocumentnoproduction():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserID")
        
        res = validatedocumentnoproduction(document_no,user_id)
        #return res.get("value")
        return res
# ValidateDocumentNoProduction For showing Public URL End -



# -----------ValidateSerialNo For showing Public URL Start +
@app.route('/webvalidateserialno',methods=['GET','POST'])
def webvalidateserialno():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        sr_no = input_json.get("Srlno")
        document_no = input_json.get("DocNo")
        
        res = validateserialno(sr_no,document_no)
        #return res.get("value")
        return res
# ValidateSerialNo For showing Public URL End -


# -----------ValidateDocBarcode For showing Public URL Start +
@app.route('/webvalidatedocbarcode',methods=['GET','POST'])
def webvalidatedocbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        doc_bar_code = input_json.get("DocBarcode")
        user_id = input_json.get("UserID")
        template_name = input_json.get("TemplateName")
        batch_name = input_json.get("BatchName")
        doc_no = input_json.get("DocNo")
               
        
        res = validatedocbarcode(doc_bar_code,user_id,template_name,batch_name,doc_no)
        #return res.get("value")
        return res
# ValidateDocBarcode For showing Public URL End -


# -----------ValidateDocBarcode For showing Public URL Start +
@app.route('/webvalidateupbarcode',methods=['GET','POST'])
def webvalidateupbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        bar_code = input_json.get("Barcode")
        
               
        
        res = validateupbarcode(bar_code)
        #return res.get("value")
        return res
# ValidateDocBarcode For showing Public URL End -


#req ="\"Barcode\":\"bar_code_\",\"PBarcode\":\"p_bar_code_\",\"OrderNo\":\"order_no_\""

# -----------ValidateUCBarcode For showing Public URL Start +
@app.route('/webvalidateucbarcode',methods=['GET','POST'])
def webvalidateucbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        bar_code = input_json.get("Barcode")
        pbar_code = input_json.get("PBarcode")
        order_no = input_json.get("OrderNo")
        
        
        res = validateucbarcode(bar_code,pbar_code,order_no)
        #return res.get("value")
        return res
# ValidateUCBarcode For showing Public URL End -



# -----------BarcodeUnPacking For showing Public URL Start +
@app.route('/webbarcodeunpacking',methods=['GET','POST'])
def webbarcodeunpacking():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        bar_code = input_json.get("ChildBarcode")
        pbar_code = input_json.get("ParentBarcode")
        user_id = input_json.get("UserID")
        
        
        res = barcodeunpacking(bar_code,pbar_code,user_id)
        #return res.get("value")
        return res
# BarcodeUnPacking For showing Public URL End -



# -----------ValidateUserPurch For showing Public URL Start +
@app.route('/webvalidateuserpurch',methods=['GET','POST'])
def webvalidateuserpurch():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        user_id = input_json.get("UserID")
        
        
        res = validateuserpurch(user_id)
        #return res.get("value")
        return res
# ValidateUserPurch For showing Public URL End -




# -----------validatedocnopurch For showing Public URL Start +
@app.route('/webvalidatedocnopurch',methods=['GET','POST'])
def webvalidatedocnopurch():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserID")
        
        
        res = validatedocnopurch(document_no,user_id)
        #return res.get("value")
        return res
# validatedocnopurch For showing Public URL End -




# -----------RMPurchaseStockTake For showing Public URL Start +
@app.route('/webrmpurchasestocktake',methods=['GET','POST'])
def webrmpurchasestocktake():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        ankit = input_json.get("ChilddBacode")
        document_no = input_json.get("DocumentNo")
        user_id = input_json.get("UserId")
        
        res = rmpurchasestocktake(ankit,document_no,user_id)
        #return res.get("value")
        return res
# RMPurchaseStockTake For showing Public URL End -



# -----------OnlineValidateLocation For showing Public URL Start +
@app.route('/webonlinevalidatelocation',methods=['GET','POST'])
def webonlinevalidatelocation():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        location_code = input_json.get("Location")
        #document_no = input_json.get("DocumentNo")
        #user_id = input_json.get("UserId")
        
        res = onlinevalidatelocation(location_code)
        #return res.get("value")
        return res
# OnlineValidateLocation For showing Public URL End -



# ----------- OnlineValidateTrnsfrShpBarcode For showing Public URL Start +
@app.route('/webonlinevalidatetrnsfrshpbarcode',methods=['GET','POST'])
def webonlinevalidatetrnsfrshpbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        barcode_code = input_json.get("Barcode")

        
        res = onlinevalidatetrnsfrshpbarcode(barcode_code)
        #return res.get("value")
        return res
# OnlineValidateTrnsfrShpBarcode For showing Public URL End -


# ----------- OnlineTransferShipmentLooseToFresh For showing Public URL Start +
@app.route('/webonlinetransfershipmentloosetofresh',methods=['GET','POST'])
def webonlinetransfershipmentloosetofresh():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        barcode_code = input_json.get("Barcode")
        transfer_order = input_json.get("TransferOrder")
        from_location = input_json.get("FromLocation")

        
        res = onlinetransfershipmentloosetofresh(barcode_code,transfer_order,from_location)
        #return res.get("value")
        return res
# OnlineTransferShipmentLooseToFresh For showing Public URL End -





# ----------- CreateTransferHeader For showing Public URL Start +
@app.route('/webcreatetransferheader',methods=['GET','POST'])
def webcreatetransferheader():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        transfer_order = input_json.get("TransferOrder")
        from_location = input_json.get("FromLocation")
        to_location = input_json.get("ToLocation")
        work_oder_no = input_json.get("WorkOderNo")
        user_id = input_json.get("UserID")

        
        res = createtransferheader(transfer_order,from_location,to_location,work_oder_no,user_id)
        #return res.get("value")
        return res
# CreateTransferHeader For showing Public URL End -


# ----------- OnlineTransferShipment For showing Public URL Start +
@app.route('/webonlinetransfershipment',methods=['GET','POST'])
def webonlinetransfershipment():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        bar_code = input_json.get("Barcode")
        transfer_order = input_json.get("TransferOrder")
        to_location = input_json.get("ToLocation")
        from_location = input_json.get("FromLocation")

        
        res = onlinetransfershipment(bar_code, transfer_order,to_location,from_location)
        #return res.get("value")
        return res
# OnlineTransferShipment For showing Public URL End -



# ----------- ValidateDocumentNo For showing Public URL Start +
@app.route('/webvalidatedocumentno',methods=['GET','POST'])
def webvalidatedocumentno():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        document_no = input_json.get("DocumentNo")
        u_id = input_json.get("UID")
        
        
        res = validatedocumentno(document_no, u_id)
        #return res.get("value")
        return res
# ValidateDocumentNo For showing Public URL End -


# ----------- ValidateArticalBarcode For showing Public URL Start +
@app.route('/webvalidatearticalbarcode',methods=['GET','POST'])
def webvalidatearticalbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        srl_no = input_json.get("Srlno")
        doc_no = input_json.get("DocNo")
        
        
        res = validatearticalbarcode(srl_no, doc_no)
        #return res.get("value")
        return res
# ValidateArticalBarcode For showing Public URL End -



# ----------- PCSStockTake For showing Public URL Start +
@app.route('/webpssstocktake',methods=['GET','POST'])
def webpssstocktake():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        srl_no = input_json.get("Srlno")
        doc_no = input_json.get("DocumentNo")
        u_id = input_json.get("UID")
        
        res = pssstocktake(srl_no, doc_no,u_id)
        #return res.get("value")
        return res
# PCSStockTake For showing Public URL End -


# ----------- ValidateReturnOrder For showing Public URL Start +
@app.route('/webvalidatereturnorder',methods=['GET','POST'])
def webvalidatereturnorder():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        return_order_no = input_json.get("ReturnOrderNo")
        
        
        res = validatereturnorder(return_order_no)
        #return res.get("value")
        return res
# ValidateReturnOrder For showing Public URL End -




# ----------- ValidateReturnBarcode For showing Public URL Start +
@app.route('/webvalidatereturnbarcode',methods=['GET','POST'])
def webvalidatereturnbarcode():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        return_order_no = input_json.get("ReturnOrderNo")
        
        
        res = validatereturnbarcode(return_order_no)
        #return res.get("value")
        return res
# ValidateReturnBarcode For showing Public URL End -


# ----------- GoodsReturn For showing Public URL Start +
@app.route('/webgoodsreturn',methods=['GET','POST'])
def webgoodsreturn():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        return_order_no = input_json.get("ReturnOrderNo")
        
        
        res = goodsreturn(return_order_no)
        #return res.get("value")
        return res
# GoodsReturn For showing Public URL End -


#******************************************** DistibutorPortal ++++++++++++++++

# ----------- ValidateWebUser For showing Public URL Start +
@app.route('/webvalidatewebuserdp',methods=['GET','POST'])
def webvalidatewebuserdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        logger.info(str(input_json))

        user_id = input_json.get("UserID")
        p_w_s = input_json.get("PWS")
        login_type = input_json.get("LoginType")
        
        
        res = validatewebuserdp(user_id,p_w_s,login_type)
        #return res.get("value")
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




# ----------- ValidateWebCustomer For showing Public URL Start +

@app.route('/webvalidatewebcustomerdp',methods=['GET','POST'])
def webvalidatewebcustomerdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        customer_code = input_json.get("CustomerCode")
        res = validatewebcustomerdp(customer_code)
        #return res.get("value")
        return res
    else:
        customer_code = request.args.get("CustomerCode")
        res = validatewebcustomerdp(customer_code)
        #return res.get("value")
        return res
# ----------- ValidateWebCustomer For showing Public URL End -


# ----------- WebUserExport For showing Public URL Start +
@app.route('/webwebuserexportdp',methods=['GET','POST'])
def webwebuserexportdp():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)

        user_id = input_json.get("UserID")
              
        
        res = webuserexport(user_id)
        #return res.get("value")
        return res
    else:
        user_id = request.args.get("UserID")
        res = webuserexport(user_id)
        # return res.get("value")
        print(res,"Response")
        return res
# ----------- WebUserExport For showing Public URL End -



# ----------- ItemCategoryExport For showing Public URL Start +
@app.route('/webitemcategoryexportdp',methods=['GET','POST'])
def webitemcategoryexportdp():
    
              
        
    res = itemcategoryexport()
    #return res.get("value")
    return res
# ----------- ItemCategoryExport For showing Public URL End -



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
        item_Category_Code = input_json.get("itemCategoryCode")
        remark = input_json.get("remark")
        print(input_json, "*************")
        res = saleorderexportapi(document_No,customer_no,item_no,s_75,s_80S,s_85M,s_90L,s_95XL,s_1002XL,s_1053XL,s_1104XL,s_1155XL,order_Type,item_Category_Code,remark)
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
        item_Category_Code = request.args.get("itemCategoryCode")
        remark = request.args.get("remark")

        res = saleorderexportapi(document_No,customer_no, item_no, s_75, s_80S, s_85M, s_90L, s_95XL, s_1002XL, s_1053XL,
                                 s_1104XL, s_1155XL, order_Type, item_Category_Code, remark)
        # return res.get("value")
        return res
# ----------- SaleOrderExportAPI For showing Public URL End -





#******************************** Mobile App Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +

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



#******************************** Mobile App End ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -








#******************************************** DistibutorPortal -----------------





# *****************************************************************************************************************************


def sendReq(vendorcode):
    url = "http://20.235.83.237:7048/BC200/ODataV4/Barcode_GetVendorBalance?Company=Bodycare"
    #url = "http://20.235.83.237:8049/BodycareLive/ODataV4/GetVendorBalance_CredentialsValidate?Company=Bodycare%20Creations%20Ltd.

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-webuserlogin END -

# -----------function name-credentialsvalidate Start +
def credentialsvalidate(user_name,pass_word):
    print(user_name,pass_word)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_CredentialsValidate?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_CredentialsValidate?Company=Bodycare%20Creations%20Ltd.";
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-credentialsvalidate END -



# -----------function name-ItemListWS Start +
def itemlistws():
    url = "http://20.235.83.237:7048/BC200/ODataV4/Company('Bodycare')/ItemListWS"
    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, auth=HttpNtlmAuth(url+"VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ItemListWS END -


url = "http://20.235.83.237:8049/BodycareLive/ODataV4/PrintBarcode_BarcodePrint?Company=Bodycare%20Creations%20Ltd.";


# -----------function name-BarcodePrint Start +
def barcodeprint(phylotno,itemno,variantcode,printreport,uom,issuedtouid,no0fbarcodes,uommrp,pricegroupcode,purstndrdqty,createdby):
    #print(user_name,pass_word)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ProcessBarcode_BarcodePrint?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/PrintBarcode_BarcodePrint?Company=Bodycare%20Creations%20Ltd.";
    req = "\"PhyLotNo\":\"phylotno_\",\"ItemNo\":\"itemno_\",\"VariantCode\":\"variantcode_\",\"PrintReport\":\"printreport_\",\"UOM\":\"uom_\",\"IssuedToUID\":\"issuedtouid_\",\"No0fBarcodes\":\"no0fbarcodes_\",\"UOMMRP\":\"uommrp_\",\"PriceGroupCode\":\"pricegroupcode_\",\"PurStndrdQty\":\"purstndrdqty_\",\"CreatedBy\":\"createdby_\""
    #req = "\"UserID\":\"user_name\",\"UserPassword\":\"pass_word\""

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-BarcodePrint END -

# -----------function name-credentialsvalidate Start +
def validateuser(user_name):
    #print(user_name)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateUser?Company=Bodycare"    
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUser?Company=Bodycare%20Creations%20Ltd."
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-validateuser END -



# -----------function name-gettemplatebatchName Start +
def gettemplatebatchname(user_name):
    #print(user_name)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_GetTemplateBatchName?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GetTemplateBatchName?Company=Bodycare%20Creations%20Ltd."
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-gettemplatebatchName END -



# -----------function name-validatedocumentnofgmanufacturing Start +
def validatedocumentnofgmanufacturing(document_no,user_id):
    #print(user_name)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoFGManufacturing?Company=Bodycare%20Creations%20Ltd."

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-validatedocumentnofgmanufacturing END -


# -----------function name-ValidateManuSerialNo Start +
def validatemanuserialno(srl_no):
    #print(user_name)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_ValidateManuSerialNo?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateManuSerialNo?Company=Bodycare%20Creations%20Ltd."

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateManuSerialNo END -


# -----------function name-FGUpdateTransferOrderQty Start +
def fgupdatetransferorderqty(srl_no,user_id):
    #print(user_name)
    #url = "http://20.235.83.237:7048/BC200/ODataV4/ScanBarcode_FGUpdateTransferOrderQty?Company=Bodycare"
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_FGUpdateTransferOrderQty?Company=Bodycare%20Creations%20Ltd."

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateCartonBarcode END -



# -----------function name-ValidateEndUser Start +
def validateenduser(end_code,user_id,carton_barcode,sales_order):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateEndUser?Company=Bodycare%20Creations%20Ltd."

    req ="\"EndCode\":\"EndCode_\",\"UserID\":\"user_id_\",\"CartonBarcode\":\"carton_barcode_\",\"SalesOrder\":\"sales_order_\""
    
    req = req.replace("EndCode_", end_code)
    req = req.replace("user_id_", user_id)
    req = req.replace("carton_barcode_", carton_barcode)
    req = req.replace("sales_order_", sales_order)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateEndUser END -




# -----------function name-ValidatePBarcode Start +
def validatepbarcode(parent_barcode):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidatePBarcode?Company=Bodycare%20Creations%20Ltd."

    req ="\"ParentBarcode\":\"parent_barcode_\""
    
    req = req.replace("parent_barcode_", parent_barcode)
   

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidatePBarcode END -


# -----------function name-ValidateCBarcode Start +
def validatecbarcode(Bar_code):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateCBarcode?Company=Bodycare%20Creations%20Ltd."

    req ="\"Barcode\":\"Bar_code_\""
    
    req = req.replace("Bar_code_", Bar_code)
   

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateCBarcode END -



# -----------function name-BarcodePacking Start +
def barcodepacking(parent_barcode,child_barcode,user_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_BarcodePacking?Company=Bodycare%20Creations%20Ltd."

    req ="\"ParentBarcode\":\"parent_barcode_\",\"ChildBarcode\":\"child_barcode_\",\"UserID\":\"user_id_\""
    
    req = req.replace("parent_barcode_", parent_barcode)
    req = req.replace("child_barcode_", child_barcode)
    req = req.replace("user_id_", user_id)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-BarcodePacking END -



# -----------function name-ValidateDocumentNoProduction Start +
def validatedocumentnoproduction(document_no,user_id):
    #print(user_name)
    
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNoProduction?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"DocumentNo\":\"document_no_\",\"UserID\":\"user_id_\""
    
    req = req.replace("document_no_", document_no)
    req = req.replace("user_id_", user_id)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateDocumentNoProduction END -



# -----------function name-ValidateSerialNo Start +
def validateserialno(barcodeserialno,document_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateSerialNo?Company=Bodycare%20Creations%20Ltd."

    req ="\"Srlno\":\"barcodeserialno_\",\"DocNo\":\"document_no_\""
    
    req = req.replace("barcodeserialno_", barcodeserialno)
    req = req.replace("document_no_", document_no)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateSerialNo END -




# -----------function name-ValidateDocBarcode Start +
def validatedocbarcode(doc_bar_code,user_id,template_name,batch_name,doc_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocBarcode?Company=Bodycare%20Creations%20Ltd."

    req ="\"DocBarcode\":\"doc_bar_code_\",\"UserID\":\"user_id_\",\"TemplateName\":\"template_name_\",\"BatchName\":\"batch_name_\",\"DocNo\":\"doc_no_\""
    
    req = req.replace("doc_bar_code_", doc_bar_code)
    req = req.replace("user_id_", user_id)
    req = req.replace("template_name_", template_name)
    req = req.replace("batch_name_", batch_name)
    req = req.replace("doc_no_", doc_no)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateDocBarcode END -



# -----------function name-ValidateUPBarcode Start +
def validateupbarcode(bar_code):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUPBarcode?Company=Bodycare%20Creations%20Ltd."

    req ="\"Barcode\":\"barcode_\""
    
    req = req.replace("barcode_", bar_code)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateUPBarcode END -



# -----------function name-ValidateUCBarcode Start +
def validateucbarcode(bar_code,pbcode,order_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUCBarcode?Company=Bodycare%20Creations%20Ltd."

    
    req ="\"Barcode\":\"bar_code_\",\"PBarcode\":\"pbcode_\",\"OrderNo\":\"order_no_\""
    
    req = req.replace("bar_code_", bar_code)
    req = req.replace("pbcode_", pbcode)
    req = req.replace("order_no_", order_no)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateUCBarcode END -



# -----------function name-BarcodeUnPacking Start +
def barcodeunpacking(bar_code,pbcode,u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_BarcodeUnPacking?Company=Bodycare%20Creations%20Ltd."

    
    req ="\"ChildBarcode\":\"bar_code_\",\"ParentBarcode\":\"pbcode_\",\"UserID\":\"u_id_\""
    
    req = req.replace("bar_code_", bar_code)
    req = req.replace("pbcode_", pbcode)
    req = req.replace("u_id_", u_id)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-BarcodeUnPacking END -



# -----------function name-ValidateUserPurch Start +
def validateuserpurch(u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateUserPurch?Company=Bodycare%20Creations%20Ltd."

    
    req ="\"UserID\":\"u_id_\""
    
    req = req.replace("u_id_", u_id)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateUserPurch END -




# -----------function name-ValidateDocNoPurch Start +
def validatedocnopurch(document_no,u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocNoPurch?Company=Bodycare%20Creations%20Ltd."

    
    req ="\"DocumentNo\":\"document_no_\",\"UserID\":\"u_id_\""
    
    req = req.replace("document_no_", document_no)
    req = req.replace("u_id_", u_id)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateDocNoPurch END -



# -----------function name-RMPurchaseStockTake Start +
def rmpurchasestocktake(ankit,document_no,u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_RMPurchaseStockTake?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"ChilddBacode\":\"ankit_\",\"DocumentNo\":\"document_no_\",\"UserId\":\"u_id_\""

    req = req.replace("document_no_",document_no)
    req = req.replace("ankit_",ankit)
    req = req.replace("u_id_",u_id)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-RMPurchaseStockTake END -


# -----------function name-OnlineValidateLocation Start +
def onlinevalidatelocation(location_Code):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineValidateLocation?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Location\":\"location_Code_\""

    req = req.replace("location_Code_",location_Code)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-OnlineValidateLocation END -




# -----------function name-OnlineValidateTrnsfrShpBarcode Start +
def onlinevalidatetrnsfrshpbarcode(bar_code):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineValidateTrnsfrShpBarcode?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Barcode\":\"bar_code_\""

    req = req.replace("bar_code_",bar_code)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-OnlineValidateTrnsfrShpBarcode END -





# -----------function name-OnlineTransferShipmentLooseToFresh Start +
def onlinetransfershipmentloosetofresh(bar_code,transfer_order,from_location):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipmentLooseToFresh?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_",bar_code)
    req = req.replace("transfer_order_",transfer_order)
    req = req.replace("from_location_",from_location)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-OnlineTransferShipmentLooseToFresh END -






# -----------function name-CreateTransferHeader Start +
def createtransferheader(transfer_order,from_location,to_location,work_oder_no,user_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_CreateTransferHeader?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"TransferOrder\":\"transfer_order_\",\"FromLocation\":\"from_location_\",\"ToLocation\":\"to_location_\",\"WorkOderNo\":\"work_oder_no_\",\"UserID\":\"user_id_\""

    req = req.replace("transfer_order_",transfer_order)
    req = req.replace("from_location_",from_location)
    req = req.replace("to_location_",to_location)
    req = req.replace("work_oder_no_",work_oder_no)
    req = req.replace("user_id_",user_id)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-CreateTransferHeader END -




# -----------function name-OnlineTransferShipment Start +
def onlinetransfershipment(bar_code,transfer_order,to_location,from_location):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipment?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"ToLocation\":\"to_location_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_",bar_code)
    req = req.replace("transfer_order_",transfer_order)
    req = req.replace("to_location_",to_location)
    req = req.replace("from_location_",from_location)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-OnlineTransferShipment END -


# -----------function name-OnlineTransferShipment Start +
def onlinetransfershipment(bar_code,transfer_order,to_location,from_location):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_OnlineTransferShipment?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Barcode\":\"bar_code_\",\"TransferOrder\":\"transfer_order_\",\"ToLocation\":\"to_location_\",\"FromLocation\":\"from_location_\""

    req = req.replace("bar_code_",bar_code)
    req = req.replace("transfer_order_",transfer_order)
    req = req.replace("to_location_",to_location)
    req = req.replace("from_location_",from_location)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-OnlineTransferShipment END -




# -----------function name-ValidateDocumentNo Start +
def validatedocumentno(document_no,u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateDocumentNo?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"DocumentNo\":\"document_no_\",\"UID\":\"u_id_\""

    req = req.replace("document_no_",document_no)
    req = req.replace("u_id_",u_id)
    


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateDocumentNo END -



# -----------function name-ValidateArticalBarcode Start +
def validatearticalbarcode(srl_no,doc_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateArticalBarcode?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Srlno\":\"srl_no_\",\"DocNo\":\"doc_no_\""

    req = req.replace("srl_no_",srl_no)
    req = req.replace("doc_no_",doc_no)

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-ValidateArticalBarcode END -



# -----------function name-PCSStockTake Start +
def pssstocktake(srl_no,doc_no,u_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_PCSStockTake?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"Srlno\":\"srl_no_\",\"DocumentNo\":\"doc_no_\",\"UID\":\"u_id_\""

    req = req.replace("srl_no_",srl_no)
    req = req.replace("doc_no_",doc_no)
    req = req.replace("u_id_",u_id)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
# function name-PCSStockTake END -





# -----------function name-ValidateReturnOrder Start +
def validatereturnorder(return_order_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateReturnOrder?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"ReturnOrderNo\":\"return_order_no_\""

    req = req.replace("return_order_no_",return_order_no)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-ValidateReturnOrder END -




# -----------function name-ValidateReturnBarcode Start +
def validatereturnbarcode(rtrn_barcode,rtrn_order_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_ValidateReturnBarcode?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"RtrnBarcode\":\"rtrn_barcode_\",\"RtrnOrderNo\":\"rtrn_order_no_\""

    req = req.replace("rtrn_barcode_",rtrn_barcode)
    req = req.replace("rtrn_order_no_",rtrn_order_no)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-ValidateReturnBarcode END -




# -----------function name-GoodsReturn Start +
def goodsreturn(rtrn_barcode,rtrn_order_no):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/ProcessBarcode_GoodsReturn?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"RtrnBarcode\":\"rtrn_barcode_\",\"RtrnOrderNo\":\"rtrn_order_no_\""

    req = req.replace("rtrn_barcode_",rtrn_barcode)
    req = req.replace("rtrn_order_no_",rtrn_order_no)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-GoodsReturn END -


#*************************************************** DistibutorPortal Function ++++++++++++++++++++++++++++++++++++++++++++++

# -----------function name-ValidateWebUser Start +
def validatewebuserdp(user_id,p_w_s,login_type):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebUser?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"UserID\":\"user_id_\",\"PWS\":\"p_w_s_\",\"LoginType\":\"login_type_\""

    req = req.replace("user_id_",user_id)
    req = req.replace("p_w_s_",p_w_s)
    req = req.replace("login_type_",login_type)


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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-ValidateWebUser END -


# -----------function name-ValidateWebCustomer Start +
def validatewebcustomerdp(customer_code):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ValidateWebCustomer?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"CustomerCode\":\"customer_code_\""

    req = req.replace("customer_code_",customer_code)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-ValidateWebCustomer END -



# -----------function name - WebUserExport Start +
def webuserexport(user_id):
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_WebUserExport?Company=Bodycare%20Creations%20Ltd."
    
    req ="\"UserID\":\"user_id_\""

    req = req.replace("user_id_",user_id)
    

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
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-WebUserExport END -


def itemcategoryexport():
    #print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/DistibutorPortal_ItemCategoryExport?Company=Bodycare%20Creations%20Ltd."
    
    req =""
    
    print(req)
    
    payload = req

    
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=HttpNtlmAuth(url+"VMServer1\Ankit", "bcpl@123"))
    print(response.text)
    outputdata = checkresponse(response.status_code, response.json())
    return outputdata
    
# function name-WebUserExport END -


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




# -----------function name - SaleOrderExportAPI Start +
def saleorderexportapi(document_No,customer_no,item_no,s_75,s_80S,s_85M,s_90L,s_95XL,s_1002XL,s_1053XL,s_1104XL,s_1155XL,order_Type,item_Category_Code,remark):
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



#******************************** Mobile App Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +

# -----------function name - ItemMasterApp Start +
def itemmasterapp(item_category_code):
    # print(user_name)
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/ItemMasterApp"
    if(item_category_code == None or item_category_code == ""):
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

#******************************** Mobile App End ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -



#*************************************************** DistibutorPortal Function -----------------------------------------------------




def checkresponse(state_code,response):
    if (state_code==200):
        return response.get("value")
    elif (state_code == 400):
        err_txt= response.get("error")
        try:
            if ("Application" in err_txt.get("code")):
                return {"Message":err_txt.get("message")}
        except Exception as e:
            return err_txt
                
    elif (state_code == 404):
        return response.get("server not available")
    elif (state_code == 408):
        return response.get("request waiting timeout")
    elif(state_code == 201):
        if(response.get("@odata.etag") != None):
            return True
        else:
            return False

app.config["DEBUG"] = True

# starting flask application
if __name__ == '__main__':
    #app.run(debug=True, port=6262)
    #app.run(host='192.168.1.44', port=6262, debug=True)
    app.run(host='127.0.0.1', port=6262, debug=True)
