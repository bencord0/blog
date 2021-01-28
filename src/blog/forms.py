from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label='Blog Search', max_length=128)
