from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder':'Write a comment...'}), label='')

    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


