from django import forms
from django.forms import modelform_factory
from .models import UserDB


UserForms=modelform_factory(UserDB,fields=["Full_Name","Phone_Number","Data_Bundle","Amount","show_custom_data_allocator"],widgets={
    "Full_Name":forms.TextInput({"autocomplete":"on","placeholder":"Enter your name",'style':'width: 100%; height: 40px;padding-left: 10px;margin-bottom:15px;border-radius: 10px; border:0.5px solid #ccc'}),
    "Phone_Number":forms.NumberInput({"autocomplete":"on","placeholder":"Enter your Momo number",'style': 'width: 100%; height: 40px;margin-bottom:15px;padding-left:10px;border-radius:10px;border:0.5px solid #ccc'}),
    "show_custom_data_allocator":forms.TextInput({"readonly":"readonly",'style': 'width: 30%; height: 30%;color: #777;background-color: #eee;border: 1px solid #ccc;'}),
    "Amount":forms.NumberInput({"autocomplete":"on","placeholder":"¢1 - ¢499","max":499,"min":0.1,"oninput":"getvalueFromAmout()","value":0.0,'style': 'width: 20%; height: 30%; margin-left:10px;gap:5px'}),
    "Data_Bundle":forms.RadioSelect(choices=UserDB.bundleAllocations,attrs={"oninput":"getradiobuttons()",'style':'width:170px; font-size:14px'})
})
