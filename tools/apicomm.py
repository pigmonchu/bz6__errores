from la_app import app
import requests

class MyAPIError(Exception):
    pass

def getAPIData(url, *params):
    url = url.format(*params)
    results = requests.get(url)

    if results.status_code == 200:
        return results.json() 
    else:
        raise MyAPIError("Errro en acceso:", results.status_code)