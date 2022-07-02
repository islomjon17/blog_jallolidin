from django import forms
from .models import *

# cats = [('Football','Football'), ('Coding','Coding'),('Intertainment','Intertainment')]



class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'author','description', 'category', 'keywords','cover', 'status')
        
        widgets = {
            
           'title':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title'}),
           'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'slug' })
            ,'author':forms.Select(attrs={'class':'form-control', 'placeholder': 'author'})
            ,'region':forms.Select(attrs={'class':'form-control', 'placeholder': 'region'})
            , 'status':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'status'})
            , 'keywords':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'keywords'})
             ,'category':forms.Select(attrs={'class':'form-control', 'placeholder': 'author'})
           , 'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'description'})
           
        } 



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        widgets = {
            
           'name':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'name'})
           
        } 