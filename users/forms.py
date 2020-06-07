from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

class Create(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')