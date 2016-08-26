# coding=gbk
from django import forms


# create forms here
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="Your e-mail address")   # email is optinal
    message = forms.CharField(widget=forms.Textarea)  # many raw text

    #会在本字段默认校验之后调用
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
