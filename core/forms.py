from django import forms


class SearchForm(forms.Form):
    destination = forms.CharField(label="Where do you want to go?", required=False)
    date = forms.DateField(label="When?", required=False)


class ReservationForm(forms.Form):
    rooms = forms.IntegerField(label="How many rooms do you want to book?", required=True)
