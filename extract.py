def getXAndY(text):
    text = text.replace(" ", "")

    idx = text.find("x")
    idy = text.find("y")

    x = int(text[0:idx])
    y = int(text[idx+1:idy])

    return x, y

def getIneq(text):
    text = text.replace(" ", "")
    idx = text.find("x")
    if idx < 0:
        x = 0
    else:
        x = int(text[0:idx])

    idy = text.find("y")
    if idy < 0:
        y = 0
    else:
        y = int(text[idx+1:idy])

    idp = text.find("<")
    case = "menor"
    if idp < 0:
        idp = text.find(">")
        case = "mayor"
    
    ifr = text.find("=")
    if ifr < 0:
        r = text[idp+1:]
    else:
        r = text[ifr+1:]

    return x, y, case, r



if __name__ == "__main__":
    text = "-3x - 4y = 23"
    print(getXAndY(text))

    text = "-6x + 9y >= 9"
    print(getIneq(text))

    text = "10x > -9"
    print(getIneq(text))

    text = "10y <= 1"
    print(getIneq(text))