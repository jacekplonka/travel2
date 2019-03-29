from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    destination = forms.CharField(label="Where do you want to go?", required=False)
    date = forms.DateField(label="When?", widget=DateInput, required=False)


class ReservationForm(forms.Form):
    rooms = forms.IntegerField(label="How many rooms do you want to book?", required=True)
