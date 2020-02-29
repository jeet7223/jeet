from django import forms
from django.core import validators

def check_for_j(value):
    if value[0].lower() != 'j':
        raise forms.ValidationError("NEED TO START WITH J")

class formName(forms.Form):
    name = forms.CharField(validators=[check_for_j])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email not same")
