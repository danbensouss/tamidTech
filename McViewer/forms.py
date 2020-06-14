from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()