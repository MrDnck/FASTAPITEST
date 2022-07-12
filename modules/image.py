import requests
from random import randrange, choice

failImage = "https://media4.giphy.com/media/l41Ym49ppcDP6iY3C/giphy.gif?cid=ecf05e47khxe758ndeg2nct5jt639z2xd1crt7k09pv4pvcy&rid=giphy.gif&ct=g"

url1 = "https://api.pexels.com/v1/search?query="
url2 = "https://api.unsplash.com/search/photos?client_id=6mOjOUhNPfnF54C-fBAWTFY6uDLSea6PSx0LNwuPOkc&page=1&query="



def retorno(img = "", alt = ""):
    if img == "":
        error = {
            "success": False,
            "alt": alt,
            "img": failImage
        }
        return error
    else:
        devolver = {
            "success": True,
            "alt": alt,
            "img": img
        }
        return devolver


def hola():
    print("hola")


def getImageSearch(names : str, apitype : str = "pexels"):
    newnames = names.replace(" ","-")
    if apitype == "pexels":
        url = url1
        try:
            header = {'Authorization': '563492ad6f91700001000001a317e3ed0f0a4aefa9e3895707935e12'}
            GET = requests.get(url+newnames , headers= header)
            result =  GET.json()
            print (retorno(choice(result["photos"])["src"]["landscape"]))
            return choice(result["photos"])["src"]["landscape"]
        except:
            print(retorno())
            return retorno()
    elif apitype == "unsplash":
        url = url2
        try:
            GET = requests.get(url+newnames)
            result =  GET.json()
            data = choice(result["results"])
            diccionario = retorno(data["urls"]["regular"], data["alt_description"])
            print(diccionario)
            return diccionario
        except:
            print(retorno())
            return retorno()
    else:
        return retorno()






