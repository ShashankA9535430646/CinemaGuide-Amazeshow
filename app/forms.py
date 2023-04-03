from django import forms
from django.contrib.auth.models import User
from .models import movies,tvshows

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class movie(forms.ModelForm):
    class Meta:
        model = movies
        fields = "__all__"
        
class tvshow(forms.ModelForm):
    class Meta:
        model = tvshows
        fields = '__all__'
        