from recipe.models import Author
from django import forms

'''
create an author
    name = models.CharField(max_length=50)
    bio = models.TextField()

create a recipe
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
'''


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    directions = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    ingredients = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
