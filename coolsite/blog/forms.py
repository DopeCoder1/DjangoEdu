from django import forms
from .models import *
from django.core.exceptions import ValidationError
# class AddPostForm(forms.Form):
    # title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    # is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")

class AddPostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Blog
        fields = ['title','slug','content','photo','is_published','category']
        widgets = {
             'title':forms.TextInput(attrs={'class':'form-input'}),
             'content':forms.Textarea(attrs={'cols':60,'rows':10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError("Длина привышает 200 символов")

        return title
