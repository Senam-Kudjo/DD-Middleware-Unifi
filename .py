from requests import get,post



from base64 import encode,b64encode,standard_b64encode

from dotenv import load_dotenv
import os
load_dotenv()

JASMIN_SMS_USERNAME=os.getenv("JASMIN_SMS_USERNAME")
JASMIN_SMS_PASSWORD=os.getenv("JASMIN_SMS_PASSWORD")

json={
    "from": "Chill Zone",
    "dlr": "no",
    "to": "233248927544",
    "content": f'You have successfully purchased 10GB at GHc20 valid till expiry(1 year).\nHere is your one-time voucher code.\nVoucher Code:1234\n'
    }

encoded_credentials =b64encode(f"{JASMIN_SMS_USERNAME}:{JASMIN_SMS_PASSWORD}".encode('utf-8')).decode('utf-8')
getencoded=f"Basic {encoded_credentials}"

headers={
    "Authorization": getencoded,
    "Content-Type": "application/json"

}

with post(url="http://66.228.38.61:8080/secure/send",json=json,headers=headers) as f:
    print(f.text)
    print(f.json())
    # self.success_url="/"


# with get(url="http://66.228.38.61:8080/secure/balance",headers=headers) as g:
#     print(g.text)
