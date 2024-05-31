import requests
import urllib3

def nepseReqParser(_dateToday):
    # Configurations for the request
    base_url = "https://www.nepalstock.com.np/api/nots/market/export/todays-price/"
    final_url = base_url + str(_dateToday)
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(final_url, headers=headers, verify=False)
    return response
