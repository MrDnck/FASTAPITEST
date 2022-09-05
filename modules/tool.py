import requests
import json



#funcions
def vMail(mail : str):
    try:
        url = f"https://verifier.meetchopra.com/verify/{mail}?token=2b1e810090b21cab8a8753ec6bd1f091fcef67e5f05d60a23922df7c294328251cafaca5c7ab48ca0acde4bcf303bdb1"
        resultado = requests.get(url)
        result = resultado.json()
        return result
    except:
        return {}

def CurrentTimeForIp(ip: str):
    url = f"https://timeapi.io/api/Time/current/ip?ipAddress={ip}"
    try:
        resultado = requests.get(url)
        result = resultado.json()
        return (result)
    except:
        result = {'year': None, 'month': None, 'day': None, 'hour': None, 'minute': None, 'seconds': None, 'milliSeconds': None, 'dateTime': None, 'date': None, 'time': None, 'timeZone': None, 'dayOfWeek': None, 'dstActive': None}
        return dict(result)


#users.update_one({"uuid_user": "6f604c1db13b48cf83e823ca40e608a2"}, {"data": "$push"})
#users.update_one({"uuid_user": "6f604c1db13b48cf83e823ca40e608a2"}, {"$set": {"data": {"$set": {"uno": "adad"}}}})
