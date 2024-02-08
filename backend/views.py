
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,get_list_or_404,resolve_url
from django.http import HttpRequest, HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from .forms import UserForms
from .models import UserDB,UniWallet_Unifi_Jasmin_Transactions_Details
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,RedirectView,TemplateView,DetailView
from django.urls import reverse,reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ImproperlyConfigured
# Create your views here.

from requests import get,post,put,exceptions
from concurrent.futures import ThreadPoolExecutor
from base64 import encode,b64encode,standard_b64encode
from time import sleep
import time as get_time_in_seconds 
from timeit import Timer,repeat,default_timer,main,timeit
from base64 import encode,b64encode,standard_b64encode
import os
from dotenv import load_dotenv
from datetime import datetime
import json
from threading import Thread
import random
import string
from glob import iglob
from heapq import nlargest

DATETIME=f"{datetime.today()}"[:19]

MTN=["024","025","053","054","055","059"]
AIRTELTIGO=["027","057","026","056"]
VODAFONE=["020","050"]
FILE=os.getcwd()
NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE="dd_pay2"
load_dotenv(list([data for idx,data in enumerate((iglob(f"{FILE}/{NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE}/**/.env",recursive=True)))] or [data for idx,data in enumerate((iglob(f"{FILE}/**/.env",recursive=True)))])[0])

TIMER=int(20)

PRIVATE_PAYSTACK_API_KEY= os.getenv("PRIVATE_PAYSTACK_API_KEY")
NANA_TWILIO_ACCOUNT_SID= os.getenv("NANA_TWILIO_ACCOUNT_SID")
NANA_TWILIO_AUTH_TOKEN= os.getenv("NANA_TWILIO_AUTH_TOKEN")
SENAM_CHILLZONE_ARKESEL_API=os.getenv("SENAM_CHILLZONE_ARKESEL_API")
UNIFI_USERNAME=os.getenv("UNIFI_USERNAME")
UNIFI_PASSWORD=os.getenv("UNIFI_PASSWORD")
JASMIN_SMS_USERNAME=os.getenv("JASMIN_SMS_USERNAME")
JASMIN_SMS_PASSWORD=os.getenv("JASMIN_SMS_PASSWORD")
UNIWALLET_API=os.getenv("UNIWALLET_API")

def store_in_different_db(self,vouchercode,uniwallet_transaction_id,payment_status,voucher_code_recieved,date_created):
    indexes=[]
    if self.request.method=="GET" and len(self.model.objects.values("id"))>0:
        for idx,data in enumerate(self.model.objects.values("id")):
            ...
            indexes.append(data["id"])
        print(True,"GET",len(self.model.objects.values("id")))
        idx_num=nlargest(n=1,iterable=indexes)[0]
        # UniWallet_Unifi_Jasmin_Transactions_Details.objects.create(Full_Name_id=idx_num,Voucher_Code=''.join(random.choice(string.digits) for x in range(13)),UniWallet_Transaction_ID=''.join(random.choice(string.ascii_letters + string.digits) for x in range(13)),Payment_Status=True,Date_Created=DATETIME)
        UniWallet_Unifi_Jasmin_Transactions_Details.objects.create(Full_Name_id=idx_num,Voucher_Code=vouchercode,UniWallet_Transaction_ID=uniwallet_transaction_id,Payment_Status=payment_status,Voucher_Code_Recieved=voucher_code_recieved,Date_Created=date_created)




def Transactions(self,transactions_validation,Amount,splitdata):

    Full_Name=self.request.POST["Full_Name"]
    Phone_Number,productId= f'233{self.request.POST["Phone_Number"].removeprefix("0")}' ,("1","MTN") if any(self.request.POST["Phone_Number"].startswith(MTN) for MTN in MTN ) else ("1","ARTLTIGO") if any(self.request.POST["Phone_Number"].startswith(AIRTELTIGO) for AIRTELTIGO in AIRTELTIGO ) else ("1","VODAFONE") if any(self.request.POST["Phone_Number"].startswith(VODAFONE) for VODAFONE in VODAFONE ) else "Phone Number Incorrect"
    ID,NETWORK=productId
    show_custom_data_allocator=self.request.POST["show_custom_data_allocator"]
    UNIWALLET_PROMPT_NAME="Debit MTN Customer"
    
    STRINGS=string.ascii_letters
    DIGITS=string.digits
    characters = STRINGS + DIGITS
        
    randomized_string = ''.join(random.choice(characters) for x in range(13))


    
    if  self.response_class.status_code==200:

        ...
        def UNIFI_JASMIN_UNIWALLET_VALIDATION_WITH_RADIO_BUTTONS_or_AMOUNT_AND_CUSTOM_DATRA_ALLOCATOR(**kwargs):

            try:
                with post("https://uniwallet.transflowitc.com/uniwallet/debit/customer",**kwargs) as UniWallet:
                    start_time=get_time_in_seconds.time()

                    if UniWallet.status_code != 200:
                        print(f" UniWallet Transactions Failed 🔴 \t{UniWallet.status_code}")

                    else:
                        print(F"UniWallet Transaction Successful 🟢{UniWallet.text} |\t{Phone_Number} |\t{ID} |\t{NETWORK}")

                        
                        try:
                            with post(url="https://197.221.84.162:8443/api/login",verify=False,cert=False,json ={"username": UNIFI_USERNAME,"password": UNIFI_PASSWORD,"remember": True,"strict": True}) as unifiAPI:

                                if unifiAPI.status_code != 200:
                                    print(f" Unifi Login Failed 🔴 \t{unifiAPI.text}")
                                else:
                                    print(f"Unifi Login Successful 🟢")

                                    # GENERATE VOUCHER CODES
                                    configure_unifiAPI=unifiAPI.headers["Set-Cookie"].split(";")
                                    unifises=configure_unifiAPI[0]
                                    csrf_token=configure_unifiAPI[3].split(",")[1]
                                    set_cookie=(f"{unifises}; {csrf_token}")

                                    unifiAPI.headers.pop("Set-Cookie")

                                    unifiAPI.headers.update({"Cookie":set_cookie,"X-Csrf-Token":(csrf_token).replace("csrf_token=","").strip()})



                                    if Amount=="0.0":
                                        print("Using: Radio Buttons - [Condition : Amount <3]")                                        
                                        # # USE DATA BUNDLES IN RADIO:

                                        if f"{splitdata}".endswith("GB"):
                       

                                            # CHECK IF DATA IS IN GIGABYTES
                                            GET_DATA_VALUE_IN_GB=round(float(splitdata.split("GB")[0]))
                                            print(f"Radio Button - [Data Size : {GET_DATA_VALUE_IN_GB}GB]")                 

                                            # USE "fourminutescountdowntimer" function to run a timer in a thread to allow checking paystack if a payment is successful or not 
                                            # CREATE TRANSACTIONS/PAYMENT
                                            def fourminutescountdowntimer():
                                                global s

                                                s=-1
                                                def time(sec):
                                                    global s
                                                    while 1:
                                                        s=s+sec

                                                        minutes,seconds=divmod(s,60)

                                                        try:
                                                            if seconds == TIMER:


                                                                ## Check if transaction is Successful from UNIWALLET
                                                            
                                                                with post(f"https://uniwallet.transflowitc.com/uniwallet/check/transaction/status/{randomized_string}",**kwargs) as verify_transactions: #RECHECK THE STATUS CODE AND THE MESSAGE IF SUCCESSFUL 
                                                                    if f'{verify_transactions.json()["status"]}'.lower().startswith("successful") == True and  f'{verify_transactions.json()["responseMessage"]}'.lower().startswith("successfully processed transaction")==True:
                                                                        with post(url="https://197.221.84.162:8443/api/s/jdjru8qh/cmd/hotspot",headers=unifiAPI.headers,verify=False,cert=False,
                                                                                            json={
                                                                                            "note":Full_Name,#Store the name of the one using the voucher
                                                                                            "n":1, #The number of voucher the user wants to create
                                                                                            "quota":1,#If quota is on then Multi-Use is selected
                                                                                            "expire_number":365, #Days it takes to expire
                                                                                            "expire_unit":1440, #60 ==hour anything less == minutes
                                                                                            "down":round(GET_DATA_VALUE_IN_GB*1000/2),
                                                                                            "up":round(GET_DATA_VALUE_IN_GB*1000/2),
                                                                                            "bytes":round(GET_DATA_VALUE_IN_GB*1000),
                                                                                            "cmd":"create-voucher"}) as createvouchers:
                                                                            if createvouchers.status_code != 200:
                                                                                    print(f"Voucher Code Failed 🔴 \t{createvouchers.text}")

                                                                            else:
                                                                                created_at=f"{datetime.today()}"[:19]
                                                                                print("Voucher Code Successful 🟢")

                                                                                # GET SPECIFIC VOUCHER GENERATED BY THE USER
                                                                                with get("https://197.221.84.162:8443/api/s/jdjru8qh/stat/voucher",headers = unifiAPI.headers,verify=False,cert=False) as getcodefromvoucher:
                                                                                        if getcodefromvoucher.status_code != 200:
                                                                                            print(f"Cross-Check Voucher Code If Exists : Failed 🔴 \t{getcodefromvoucher.text}")
                                                                                        else:
                                                                                            print("Cross-Check Voucher Code If Exists : Successful 🟢")

                                                                                        
                                                                                            for idx,data in enumerate(getcodefromvoucher.json()["data"]):
                                                                                               
                                                                                                REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                print(f"{REMAINING_TIME=}")
  
                                                                                                try:
                                                                                                    if data["note"]==Full_Name and  datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S')==created_at:
                                                                                                       
                                                                                                        REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                        print(f"{REMAINING_TIME=}")



                                                                                                        # JASMIN SMS API For Sending voucher
                                                                                                        

                                                                                                        json={
                                                                                                            "from": "Chill Zone",
                                                                                                            "dlr": "no",
                                                                                                            "to": Phone_Number,
                                                                                                            "content": f'You have successfully purchased {GET_DATA_VALUE_IN_GB}GB at GHc{transactions_validation}.\nHere is your one-time voucher code.\nVoucher Code:{data["code"]}\n'
                                                                                                            
                                                                                                        }

                                                                                                        encoded_credentials =b64encode(f"{JASMIN_SMS_USERNAME}:{JASMIN_SMS_PASSWORD}".encode('utf-8')).decode('utf-8')
                                                                                                        getencoded=f"Basic {encoded_credentials}"

                                                                                                        headers={
                                                                                                            "Authorization": getencoded,
                                                                                                            "Content-Type": "application/json"

                                                                                                        }

                                                                                                        with post(url="http://66.228.38.61:8080/secure/send",json=json,headers=headers) as f:
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            end_time_for_radio_GB=get_time_in_seconds.time()
                                                                                                            print(f"Completed In: {end_time_for_radio_GB-start_time}")
                                                                                                            print(f.text)
                                                                                                            print("Voucher Code Recieved By Client 🟢 ")
                                                                                                            with open("unifi.txt","+a") as ff:
                                                                                                                ff.write(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} \n\n')
                                                                                                                print(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} ')
                                                                                                               # store_in_different_db(self,data["code"],verify_transactions["uniwalletTransactionId"],True,True,datetime.now())
                                                                                                            

                                                                                                            break

                                                                                                except KeyError:
                                                                                                    print("Does not Exist")
                                                                                                    ...
                                                                                                except UserWarning:
                                                                                                    ...

                                                                    elif f'{verify_transactions.json()["status"]}'.lower().startswith("process") == True:
                                                                        print(verify_transactions.json()["status"])
                                                                        fourminutescountdowntimer()


                                                                    else:
                                                                        print(verify_transactions.json()["status"])
                                                                       # store_in_different_db(self,''.join(random.choice(string.digits) for x in range(13)),''.join(random.choice(string.ascii_letters + string.digits) for x in range(13)),False,False,datetime.now())
                                                                        break
                                                                    break
                                                            else:
                                                                print(seconds)
                                              

                                                        except:
                                                            ...
                                                        sleep(1)

                                                time(1)
                                            T=Thread(target=fourminutescountdowntimer,name="fourminutescountdowntimer",daemon=True)
                                            T.start()

                                                
                                        else:

                                            # CHECK IF DATA IS IN MEGABYTES
                                            GET_DATA_VALUE_IN_MB=round(float(f"{splitdata}".split("MB")[0]))
                                            print(f"Radio Button - [Data Size : {GET_DATA_VALUE_IN_MB}MB]")                                        

                                            def fourminutescountdowntimer():
                                                global s

                                                s=-1
                                                def time(sec):
                                                    global s
                                                    while 1:
                                                        s=s+sec

                                                        minutes,seconds=divmod(s,60)

                                                        try:
                                                            if seconds == TIMER:


                                                                ## Check if transaction is Successful from UNIWALLET
                                                            
                                                                with post(f"https://uniwallet.transflowitc.com/uniwallet/check/transaction/status/{randomized_string}",**kwargs) as verify_transactions: #RECHECK THE STATUS CODE AND THE MESSAGE IF SUCCESSFUL 
                                                                    if f'{verify_transactions.json()["status"]}'.lower().startswith("successful") == True and  f'{verify_transactions.json()["responseMessage"]}'.lower().startswith("successfully processed transaction")==True:
                                                                        with post(url="https://197.221.84.162:8443/api/s/jdjru8qh/cmd/hotspot",headers=unifiAPI.headers,verify=False,cert=False,
                                                                                            json={
                                                                                            "note":Full_Name,#Store the name of the one using the voucher
                                                                                            "n":1, #The number of voucher the user wants to create
                                                                                            "quota":1,#If quota is on then Multi-Use is selected
                                                                                            "expire_number":365, #Days it takes to expire
                                                                                            "expire_unit":1440, #60 ==hour anything less == minutes
                                                                                            "down":round(GET_DATA_VALUE_IN_MB/2),
                                                                                            "up":round(GET_DATA_VALUE_IN_MB/2),
                                                                                            "bytes":round(GET_DATA_VALUE_IN_MB),
                                                                                            "cmd":"create-voucher"}) as createvouchers:
                                                                            if createvouchers.status_code != 200:
                                                                                    print(f"Voucher Code Failed 🔴 \t{createvouchers.text}")

                                                                            else:
                                                                                created_at=f"{datetime.today()}"[:19]
                                                                                print("Voucher Code Successful 🟢")

                                                                                # GET SPECIFIC VOUCHER GENERATED BY THE USER
                                                                                with get("https://197.221.84.162:8443/api/s/jdjru8qh/stat/voucher",headers = unifiAPI.headers,verify=False,cert=False) as getcodefromvoucher:
                                                                                        if getcodefromvoucher.status_code != 200:
                                                                                            print(f"Cross-Check Voucher Code If Exists : Failed 🔴 \t{getcodefromvoucher.text}")
                                                                                        else:
                                                                                            print("Cross-Check Voucher Code If Exists : Successful 🟢")

                                                                                        
                                                                                            for idx,data in enumerate(getcodefromvoucher.json()["data"]):
                                                                                                
                                                                                                REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                print(f"{REMAINING_TIME=}")

                                                                                                try:
                                                                                                    if data["note"]==Full_Name and  datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S')==created_at:
                                                                                                        
                                                                                                        REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                        print(f"{REMAINING_TIME=}")



                                                                                                        # JASMIN SMS API For Sending voucher
                                                                                                        

                                                                                                        json={
                                                                                                            "from": "Chill Zone",
                                                                                                            "dlr": "no",
                                                                                                            "to": Phone_Number,
                                                                                                            "content": f'You have successfully purchased {GET_DATA_VALUE_IN_MB}MB at GHc{transactions_validation}.\nHere is your one-time voucher code.\nVoucher Code:{data["code"]}\n'
                                                                                                        
                                                                                                        }

                                                                                                        encoded_credentials =b64encode(f"{JASMIN_SMS_USERNAME}:{JASMIN_SMS_PASSWORD}".encode('utf-8')).decode('utf-8')
                                                                                                        getencoded=f"Basic {encoded_credentials}"

                                                                                                        headers={
                                                                                                            "Authorization": getencoded,
                                                                                                            "Content-Type": "application/json"

                                                                                                        }

                                                                                                        with post(url="http://66.228.38.61:8080/secure/send",json=json,headers=headers) as f:
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            end_time_for_radio_MB=get_time_in_seconds.time()
                                                                                                            print(f"Completed In: {end_time_for_radio_MB-start_time}")
                                                                                                            print(f.text)
                                                                                                            print("Voucher Code Recieved By Client 🟢 ")
                                                                                                            with open("unifi.txt","+a") as ff:
                                                                                                                ff.write(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} \n\n')
                                                                                                                print(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} ')
                                                                                                               # store_in_different_db(self,data["code"],verify_transactions["uniwalletTransactionId"],True,True,datetime.now())
                                                                                                            
                                                                                                            break

                                                                                                
                                                                                                except KeyError:
                                                                                                    print("Does not Exist")
                                                                                                    ...
                                                                                                except UserWarning:
                                                                                                    ...

                                                                    elif f'{verify_transactions.json()["status"]}'.lower().startswith("process") == True:
                                                                        print(verify_transactions.json()["status"])
                                                                        fourminutescountdowntimer()


                                                                    else:
                                                                        print(verify_transactions.json()["status"])
                                                                       # store_in_different_db(self,''.join(random.choice(string.digits) for x in range(13)),''.join(random.choice(string.ascii_letters + string.digits) for x in range(13)),False,False,datetime.now())
                                                                        break
                                                                    break
                                                            else:
                                                                print(seconds)

                                                        except:
                                                            ...
                                                        sleep(1)

                                                time(1)
                                            T=Thread(target=fourminutescountdowntimer,name="fourminutescountdowntimer",daemon=True)
                                            T.start()

                                        self.success_url="/"


                                    else:
                                        # USE VALUE OF AMOUNT TO MAKE PAYMENT TO UNIWALLET and SHOW_CUSTOM_DATA_ALLOCATOR
                                        print("Using: Custom Data Allocator - [Condition : Amount >2]")                                        
                                        if show_custom_data_allocator.endswith("GB"):
                                            GET_DATA_VALUE_IN_GB=round(float(show_custom_data_allocator.split("GB")[0]))
                                            print(f"Custom Data Allocator - [Data Size :{GET_DATA_VALUE_IN_GB}GB]")                                        

                                            def fourminutescountdowntimer():
                                                global s

                                                s=-1
                                                def time(sec):
                                                    global s
                                                    while 1:
                                                        s=s+sec

                                                        minutes,seconds=divmod(s,60)

                                                        try:
                                                            if seconds == TIMER:


                                                                ## Check if transaction is Successful from UNIWALLET
                                                            
                                                                with post(f"https://uniwallet.transflowitc.com/uniwallet/check/transaction/status/{randomized_string}",**kwargs) as verify_transactions: #RECHECK THE STATUS CODE AND THE MESSAGE IF SUCCESSFUL 
                                                                    if f'{verify_transactions.json()["status"]}'.lower().startswith("successful") == True and  f'{verify_transactions.json()["responseMessage"]}'.lower().startswith("successfully processed transaction")==True:
                                                                        with post(url="https://197.221.84.162:8443/api/s/jdjru8qh/cmd/hotspot",headers=unifiAPI.headers,verify=False,cert=False,
                                                                                            json={
                                                                                            "note":Full_Name,#Store the name of the one using the voucher
                                                                                            "n":1, #The number of voucher the user wants to create
                                                                                            "quota":1,#If quota is on then Multi-Use is selected
                                                                                            "expire_number":365, #Days it takes to expire
                                                                                            "expire_unit":1440, #60 ==hour anything less == minutes
                                                                                            "down":round(GET_DATA_VALUE_IN_GB*1000/2),
                                                                                            "up":round(GET_DATA_VALUE_IN_GB*1000/2),
                                                                                            "bytes":round(GET_DATA_VALUE_IN_GB*1000),
                                                                                            "cmd":"create-voucher"}) as createvouchers:
                                                                            if createvouchers.status_code != 200:
                                                                                    print(f"Voucher Code Failed 🔴 \t{createvouchers.text}")

                                                                            else:
                                                                                created_at=f"{datetime.today()}"[:19]
                                                                                print("Voucher Code Successful 🟢")

                                                                                # GET SPECIFIC VOUCHER GENERATED BY THE USER
                                                                                with get("https://197.221.84.162:8443/api/s/jdjru8qh/stat/voucher",headers = unifiAPI.headers,verify=False,cert=False) as getcodefromvoucher:
                                                                                        if getcodefromvoucher.status_code != 200:
                                                                                            print(f"Cross-Check Voucher Code If Exists : Failed 🔴 \t{getcodefromvoucher.text}")
                                                                                        else:
                                                                                            print("Cross-Check Voucher Code If Exists : Successful 🟢")

                                                                                        
                                                                                            for idx,data in enumerate(getcodefromvoucher.json()["data"]):
                                                                                                
                                                                                                REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                print(f"{REMAINING_TIME=}")

                                                                                                
                                                                                                try:


                                                                                                    if data["note"]==Full_Name and  datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S')==created_at:

                                                                                                        REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                        print(f"{REMAINING_TIME=}")


                                                                                                        # JASMIN SMS API For Sending voucher
                                                                                                        

                                                                                                        json={
                                                                                                            "from": "Chill Zone",
                                                                                                            "dlr": "no",
                                                                                                            "to": Phone_Number,
                                                                                                            "content": f'You have successfully purchased {GET_DATA_VALUE_IN_GB}GB at GHc{transactions_validation}.\nHere is your one-time voucher code.\nVoucher Code:{data["code"]}\n'

                                                                                                        }

                                                                                                        encoded_credentials =b64encode(f"{JASMIN_SMS_USERNAME}:{JASMIN_SMS_PASSWORD}".encode('utf-8')).decode('utf-8')
                                                                                                        getencoded=f"Basic {encoded_credentials}"

                                                                                                        headers={
                                                                                                            "Authorization": getencoded,
                                                                                                            "Content-Type": "application/json"

                                                                                                        }

                                                                                                        with post(url="http://66.228.38.61:8080/secure/send",json=json,headers=headers) as f:
                                                                                                           
                                                                                                            

                                                                                                            end_time_for_custom_GB=get_time_in_seconds.time()
                                                                                                            print(f"Completed In: {end_time_for_custom_GB-start_time}")        
                                                                                                            print(f.text)
                                                                                                            print("Voucher Code Recieved By Client 🟢 ")
                                                                                                            with open("unifi.txt","+a") as ff:
                                                                                                                ff.write(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} \n\n')
                                                                                                                print(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} ')
                                                                                                               # store_in_different_db(self,data["code"],verify_transactions["uniwalletTransactionId"],True,True,datetime.now())
                                                                                                            
                                                                                                            break


                                                                                                except KeyError:
                                                                                                    print("Does not Exist")
                                                                                                    ...
                                                                                                except UserWarning:
                                                                                                    ...

                                                                    elif f'{verify_transactions.json()["status"]}'.lower().startswith("process") == True:
                                                                        print(verify_transactions.json()["status"])
                                                                        fourminutescountdowntimer()

                                                                    else:
                                                                        print(verify_transactions.json()["status"])
                                                                       # store_in_different_db(self,''.join(random.choice(string.digits) for x in range(13)),''.join(random.choice(string.ascii_letters + string.digits) for x in range(13)),False,False,datetime.now())
                                                                        break
                                                                    break
                                                            else:
                                                                print(seconds)
                                               

                                                        except:
                                                            ...
                                                        sleep(1)

                                                time(1)
                                            T=Thread(target=fourminutescountdowntimer,name="fourminutescountdowntimer",daemon=True)
                                            T.start()
                                            

                                        else:
                                            # VALIDATE AMOUNT & CUSTOM DATA ALLOCATOR
                                            GET_DATA_VALUE_IN_MB=round(float(show_custom_data_allocator.split("MB")[0]))
                                            print(f"Custom Data Allocator - [Data Size :{GET_DATA_VALUE_IN_MB}MB]")

                                            # USE "fourminutescountdowntimer" function to run a timer in a thread to allow checking paystack if a payment is successful or not 
                                            def fourminutescountdowntimer():
                                                global s

                                                s=-1
                                                def time(sec):
                                                    global s
                                                    while 1:
                                                        s=s+sec

                                                        minutes,seconds=divmod(s,60)

                                                        try:
                                                            if seconds == TIMER:



                                                                ## Check if transaction is Successful from UNIWALLET
                                                            
                                                                with post(f"https://uniwallet.transflowitc.com/uniwallet/check/transaction/status/{randomized_string}",**kwargs) as verify_transactions: #RECHECK THE STATUS CODE AND THE MESSAGE IF SUCCESSFUL 
                                                                    if f'{verify_transactions.json()["status"]}'.lower().startswith("successful") == True and  f'{verify_transactions.json()["responseMessage"]}'.lower().startswith("successfully processed transaction")==True:
                                                                        with post(url="https://197.221.84.162:8443/api/s/jdjru8qh/cmd/hotspot",headers=unifiAPI.headers,verify=False,cert=False,
                                                                                            json={
                                                                                            "note":Full_Name,#Store the name of the one using the voucher
                                                                                            "n":1, #The number of voucher the user wants to create
                                                                                            "quota":1,#If quota is on then Multi-Use is selected
                                                                                            "expire_number":365, #Days it takes to expire
                                                                                            "expire_unit":1440, #60 ==hour anything less == minutes
                                                                                            "down":round(GET_DATA_VALUE_IN_MB/2),
                                                                                            "up":round(GET_DATA_VALUE_IN_MB/2),
                                                                                            "bytes":round(GET_DATA_VALUE_IN_MB),
                                                                                            "cmd":"create-voucher"}) as createvouchers:
                                                                            if createvouchers.status_code != 200:
                                                                                    print(f"Voucher Code Failed 🔴 \t{createvouchers.text}")

                                                                            else:
                                                                                created_at=f"{datetime.today()}"[:19]
                                                                                print("Voucher Code Successful 🟢")

                                                                                # GET SPECIFIC VOUCHER GENERATED BY THE USER
                                                                                with get("https://197.221.84.162:8443/api/s/jdjru8qh/stat/voucher",headers = unifiAPI.headers,verify=False,cert=False) as getcodefromvoucher:
                                                                                        if getcodefromvoucher.status_code != 200:
                                                                                            print(f"Cross-Check Voucher Code If Exists : Failed 🔴 \t{getcodefromvoucher.text}")
                                                                                        else:
                                                                                            print("Cross-Check Voucher Code If Exists : Successful 🟢")

                                                                                        
                                                                                            for idx,data in enumerate(getcodefromvoucher.json()["data"]):
                                                                                                
                                                                                                REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                print(f"{REMAINING_TIME=}")

                                                                                                try:

                                                                                                    if data["note"]==Full_Name and  datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S')==created_at:
                                                                                                       
                                                                                                        REMAINING_TIME=(datetime.strptime(datetime.utcfromtimestamp(data["create_time"]).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")-datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"))
                                                                                                        print(f"{REMAINING_TIME=}")


                                                                                                        # JASMIN SMS API For Sending voucher
                                                                                                        

                                                                                                        json={
                                                                                                            "from": "Chill Zone",
                                                                                                            "dlr": "no",
                                                                                                            "to": Phone_Number,
                                                                                                            "content": f'You have successfully purchased {GET_DATA_VALUE_IN_MB}MB at GHc{transactions_validation}.\nHere is your one-time voucher code.\nVoucher Code:{data["code"]}\n' 
                                                                                                            
                                                                                                        }

                                                                                                        encoded_credentials =b64encode(f"{JASMIN_SMS_USERNAME}:{JASMIN_SMS_PASSWORD}".encode('utf-8')).decode('utf-8')
                                                                                                        getencoded=f"Basic {encoded_credentials}"

                                                                                                        headers={
                                                                                                            "Authorization": getencoded,
                                                                                                            "Content-Type": "application/json"

                                                                                                        }

                                                                                                        with post(url="http://66.228.38.61:8080/secure/send",json=json,headers=headers) as f:
                                                                                                           
                                                                                                            
                                                                                                           
                                                                                                            end_time_for_custom_MB=get_time_in_seconds.time()
                                                                                                            print(f"Completed In: {end_time_for_custom_MB-start_time}")
                                                                                                            print(f.text)
                                                                                                            print("Voucher Code Recieved By Client 🟢 ")
                                                                                                            with open("unifi.txt","+a") as ff:
                                                                                                                ff.write(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} \n\n')
                                                                                                                print(f'Name:{data["note"]}\nVoucher Code:{data["code"]}\nCreated At: {datetime.utcfromtimestamp(data["create_time"]).strftime("%Y-%m-%d %H:%M:%S")} ')
                                                                                                               # store_in_different_db(self,data["code"],verify_transactions["uniwalletTransactionId"],True,True,datetime.now())
                                                                                                            
                                                                                                            break


                                                                                                except KeyError:
                                                                                                    print("Does not Exist")
                                                                                                    ...
                                                                                                except UserWarning:
                                                                                                    ...

                                                                    elif f'{verify_transactions.json()["status"]}'.lower().startswith("process") == True:
                                                                        print(verify_transactions.json()["status"])
                                                                        fourminutescountdowntimer()


                                                                    else:
                                                                        print(verify_transactions.json()["status"])
                                                                       # store_in_different_db(self,''.join(random.choice(string.digits) for x in range(13)),''.join(random.choice(string.ascii_letters + string.digits) for x in range(13)),False,False,datetime.now())
                                                                        break
                                                                    break
                                                            else:
                                                                print(seconds)
                                                

                                                        except:
                                                            ...
                                                        sleep(1)

                                                time(1)
                                            T=Thread(target=fourminutescountdowntimer,name="fourminutescountdowntimer",daemon=True)
                                            T.start()

                                        self.success_url="/"
                        except exceptions.ConnectionError:
                            print("UNIFI Connection Error! 🔴")
                            print(f"{locals()}")
                            # self.success_url="/"
                            ...

            except exceptions.ConnectionError:
                print("UNIWALLET Connection Error! 🔴")
                print(f"{locals()}")
                # self.success_url="/"

            ...                                                   


        with ThreadPoolExecutor(10) as executeParallel:
            startExecution=executeParallel.submit(UNIFI_JASMIN_UNIWALLET_VALIDATION_WITH_RADIO_BUTTONS_or_AMOUNT_AND_CUSTOM_DATRA_ALLOCATOR,
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "merchantId": "3488",
                    "productId": ID,
                    "refNo": randomized_string,
                    "msisdn": Phone_Number,
                    "amount":transactions_validation,
                    "network": NETWORK,
                    "narration": UNIWALLET_PROMPT_NAME,
                    "apiKey": UNIWALLET_API
                }
            )
            startExecution.result()  




class index:



    class paywithPaystack(CreateView):

        try:
            model = UserDB
            form_class = UserForms
            template_name = 'index.html'

            def get_form_kwargs(self):
                
                kwargs = super().get_form_kwargs()

                try:
                    try:
                        Amount=self.request.POST["Amount"]

                        Data_Bundle=self.request.POST["Data_Bundle"]
                        splitamount,splitdata=Data_Bundle.split("_GHS__")

 
                        transactions_validation=splitamount 
                        print(f"{splitamount=}")
                        Transactions(self,transactions_validation,Amount,splitdata)

                    except ValueError:
                        ...
 
                        transactions_validation=Amount 
                        print(f"{Amount=}")
                        Transactions(self,transactions_validation,Amount,None)
 
                except MultiValueDictKeyError:
                    ...

                return kwargs
    
        except ImproperlyConfigured:
            ...
