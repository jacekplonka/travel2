from django import forms


class SearchForm(forms.Form):
    destination = forms.CharField(label="Where do you want to go?", required=False)
    date = forms.DateField(label="When?", required=False)
