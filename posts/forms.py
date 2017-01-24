from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            # "author",
            "content",
            "image"
        ]

    # def clean_image(self):
    #     height = int(self.cleaned_data.get('height'))
    #     width = int(self.cleaned_data.get('width'))
    #     if height < 700:
    #         if width < 900:
    #             raise forms.ValidationError("image is too small")
