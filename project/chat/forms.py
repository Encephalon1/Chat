from django import forms
from .models import MyUser


class Avatar(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('picture',)
