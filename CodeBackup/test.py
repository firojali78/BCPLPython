a = {
    "@odata.context": "http://20.235.83.237:7048/BC200/ODataV4/$metadata#Edm.String",
    "value": "{\"id\":\"1\",\"Success\":\"True\",\"UserTemplateName\":\"ITEM\",\"UserBatchName\":\"DEFAULT\"}"
}
b = a.get("value")
print(b)