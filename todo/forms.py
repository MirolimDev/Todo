from django import forms
from django.forms import ModelForm, fields

from .models import CreateModel

class CreatorForm(ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Yangi topshiriq qoshish....'}))
    class Meta:
        model = CreateModel
        fields = '__all__'
