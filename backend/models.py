from django.db import models

# Create your models here.
class UserDB(models.Model):
    Full_Name=models.CharField(unique=False,max_length=40,default="")
    Phone_Number=models.CharField(unique=False,max_length=10)
    Amount=models.DecimalField(max_digits=5,decimal_places=2,max_length=3,null=True,blank=True)
    bundleAllocations=models.TextChoices("","3_GHS__340MB 5_GHS__740MB 10_GHS__1GB")
    Data_Bundle=models.CharField(max_length=15,choices=bundleAllocations.choices,blank=True,default="")
    show_custom_data_allocator=models.CharField(unique=False,max_length=9,null=True,blank=True)

    def __str__(self) -> str:
        return self.Phone_Number

# Create your models here.
class UniWallet_Unifi_Jasmin_Transactions_Details(models.Model):
    Phone_Number=models.ForeignKey(UserDB,models.CASCADE,unique=False,max_length=40,default="")
    Voucher_Code=models.PositiveIntegerField(editable=True,unique=True,null=True,auto_created=True)
    UniWallet_Transaction_ID=models.CharField(max_length=15,default="",editable=True,unique=True,null=True,auto_created=True)
    Payment_Status=models.BooleanField(auto_created=True,default=False)
    Voucher_Code_Recieved=models.BooleanField(auto_created=True,default=False)
    Date_Created=models.DateTimeField(auto_created=True,auto_now=True)
    def __str__(self) -> str:
        return f"{self.Phone_Number}"

