import uiautomator2 as u2


def unitToNumber(x):
    str = x
    findstr = str.find(".")
    if findstr == -1:
        return str
    else:    
        endstr = (str[-1:])    
        splitstr = str.split('.')
        strS = splitstr[0]
        if endstr == "K":
            strE = "000"
        elif endstr == "M":
            strE = "000000"    
        return (strS+strE)
# def clickElm(elm):
#     click = device_encoding(eml).click()