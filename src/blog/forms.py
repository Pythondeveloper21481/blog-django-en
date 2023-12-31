from django import forms
from .models import Comment, Post

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name', 'email', 'body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label = 'Titre de blog')
    content = forms.CharField(label='Text du blog ', widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'content']