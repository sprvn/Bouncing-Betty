import requests
import json

def checkVPN():
    r = requests.get('https://am.i.mullvad.net/json')

    if r.status_code != 200:
        return False

    try:
        resp = json.loads(r.text)
    except:
        return False

    if 'mullvad_exit_ip' not in resp:
        return False

    if resp['mullvad_exit_ip'] == True:
        return True
    else:
        return False

