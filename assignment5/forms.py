from django import forms
from django.core import validators
from assignment5.models import Invitation, Comments


class Invites(forms.ModelForm):
    class Meta():
        guest1 = '1 Guest'
        guest2 = '2 Guest'
        guest3 = '3 Guest'
        guest4 = '4 Guest'
        guest_number = [
            (guest1, '1 Guest'),
            (guest2, '2 Guest'),
            (guest3, '3 Guest'),
            (guest4, '4 Guest'),
        ]
        model = Invitation
        fields = {'full_name', 'email', 'guest', 'message'}
        exclude = ('time',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'guest': forms.Select(attrs={'class':'form-control'}, choices=guest_number),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'}),
        }



class Contact(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Subject'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Message'}))

class UserComment(forms.ModelForm):
    class Meta():
        model = Comments
        fields = {'comment',}
        exclude = ('time',)
        widgets = {
            'comment':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Comment', 'row':'50'}),
        }