from django import forms
from posts.models import *


class PostCreatForm(forms.Form):
    
    title = forms.CharField()
    body = forms.Textarea()
    photo = forms.ImageField()
    
class PostModelform(forms.ModelForm): # most use
    class Meta:
        model = customer
        fields = ['title','body','photo'] # this sequence