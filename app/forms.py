from django import forms
from django.core import validators
def validate_for_a(Svalue):
    if Svalue[0].lower=='a':
        raise forms.ValidationError('it is a validation')

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError("first letter should not be a")


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validate_for_a])
    Sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9\d{9}]')])
 

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    


    def clean(self):
       e=self.cleaned_data['email']
       re=self.cleaned_data['remail']
       if e!=re:
           raise forms.ValidationError['email is not matched']


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
           raise forms.ValidationError('bot')





