__author__ = 'cyberrick'
from django import forms


class CommentForm(forms.Form):
    blog = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea, label="")