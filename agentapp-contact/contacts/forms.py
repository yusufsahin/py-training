from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Adınız ve soyadınız"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "ornek@eposta.com"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Kısa konu başlığı"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "placeholder": "Mesajınızı yazın"}
            ),
        }
