from django import forms

from .models import Reviews


class ReviewForms(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")