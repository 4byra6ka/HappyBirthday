from django import forms

from subscriptions.models import Subscriptions


class SubscriptionsCreateForm(forms.ModelForm):
    notification = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'datetime-local'}))

    class Meta:
        model = Subscriptions
        fields = ('notification',)
