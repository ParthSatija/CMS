from django import forms
from models import Subscriber
from models import Crisis

class CrisisCreateForm(forms.ModelForm):
    class Meta:
        model=Crisis
        exclude=['isActive','date','time']

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = "__all__"
