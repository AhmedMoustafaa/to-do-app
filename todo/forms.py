from django.forms import ModelForm, TextInput
from.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('__all__')
        widgets = {
            'item': TextInput(attrs={'placeholder': 'Add Item', 'id':'vlaue', 'name':'value', 'class':"form-control"}),
        }
        error_messages = {
            'item': {
                'max_length': ('The item is too long'),
            },
        }
        labels = {
            'item': (''),
        }