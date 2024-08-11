from django import forms
from . models import Articles


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ['name', 'description', 'price', 'actif', 'slug', 'image']
        
        
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not "veve" in name:
            raise forms.ValidationError("Ajouter le nom veve")
        else:
            return name