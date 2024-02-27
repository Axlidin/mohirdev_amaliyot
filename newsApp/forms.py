from django import forms
from .models import Contact
class ContactForms(forms.ModelForm):#Form xam bo'laveradi

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'message']
        fields = "__all__"#xammasini