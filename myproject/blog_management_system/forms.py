from django import forms
from .models import BlogPostModel,Category, CommentModel

class BlogPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        required=True 
    )

    class Meta:
        model = BlogPostModel
        fields = ['title', 'content', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']


