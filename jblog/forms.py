from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'author','description', 'category', 'keywords','cover', 'status')
        
        widgets = {
            
           'title':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title'}),
           'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'slug' })
            ,'author':forms.Select(attrs={'class':'form-control', 'placeholder': 'author'})
            , 'status':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'status'})
            , 'keywords':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'keywords'})
            , 'category': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'category'})
           , 'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'description'})
           
        } 