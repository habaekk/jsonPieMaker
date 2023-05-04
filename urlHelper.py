from K import K

def urlHelper(month, day, year):
    url = ""

    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day

    keyManager = K()
    key = keyManager.getKey()

    urlFront = "https://apis.data.go.kr/B090041/openapi/service/LrsrCldInfoService/getLunCalInfo?"
    urlQuery = "solYear=" + year + "&solMonth=" + month + "&solDay=" + day + "&ServiceKey=" + key
    
    url = urlFront + urlQuery

    return url