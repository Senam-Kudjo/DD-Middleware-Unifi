from django.contrib import admin
from .models import UserDB,UniWallet_Unifi_Jasmin_Transactions_Details
# Register your models here.


class UserDBAdmin(admin.ModelAdmin):
    list_display = ['Full_Name',"Phone_Number","Data_Bundle","Amount","show_custom_data_allocator"]
admin.site.register(UserDB,UserDBAdmin)


class UniWallet_Unifi_Jasmin_Transactions_DetailsDBAdmin(admin.ModelAdmin):
    list_display = ["Phone_Number","Voucher_Code","UniWallet_Transaction_ID","Payment_Status","Voucher_Code_Recieved","Date_Created"]

admin.site.register(UniWallet_Unifi_Jasmin_Transactions_Details,UniWallet_Unifi_Jasmin_Transactions_DetailsDBAdmin)
