from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(), label="タイトル")
    body = forms.CharField(widget=forms.Textarea(), label="本文")
    image = forms.ImageField(label="画像")

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ["content","body","image",]
