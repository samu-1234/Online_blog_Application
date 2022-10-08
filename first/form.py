from dataclasses import field
from django import forms
from django.forms import models
from django.db import models
from .models import BlogInfo

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogInfo
        fields='__all__'
        # fields=['content']