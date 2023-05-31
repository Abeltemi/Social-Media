from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'captions')
    
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body', 'posted_by')