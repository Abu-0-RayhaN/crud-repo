from django import forms
from .models import userpost
class customerform(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    address= forms.CharField(label='Your name',widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Address here','row':'03','cols':'50'}),error_messages={'required':'Must enter the right address'})

    class Meta:
        model=userpost
        fields = '__all__'
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email here'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Your contact number'}),
            'department':forms.Select(attrs={'class':'form-control',}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'lanugage':forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),

        }
        error_messages = {
            'gender' : { 'required' : 'Must Select a Gender'},
            'email' : { 'required' : 'Enter Correct Email'},
            'language' : { 'required' : 'Select Language You Know'},
        }