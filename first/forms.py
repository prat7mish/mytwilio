from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["number"]
        labels={"number":"My Number"}

class PostForm(forms.Form):
    Enter_Otp=forms.CharField()