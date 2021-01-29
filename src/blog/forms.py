from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=128,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search'},
        ),
    )
