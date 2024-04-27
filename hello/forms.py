from django import forms
from .models import Feedback
from .models import Product
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
class adLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
class adSignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }