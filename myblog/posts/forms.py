from django import forms
from posts.models import customer


class PostCreatForm(forms.Form):
    
    title = forms.CharField()
    body = forms.Textarea()
    photo = forms.ImageField()
    
class PostModelform(forms.ModelForm): # most use
    class Meta:
        model = customer
        fields = ['title','body','photo'] # this sequence
        


# ====================== Day 10 Django Day 5 ====================

        
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['title','body','photo']  #day 10