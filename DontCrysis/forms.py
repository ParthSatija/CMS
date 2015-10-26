from django import forms
from models import Subscriber
from models import Crisis
from models import ReportReceiver

class CrisisCreateForm(forms.ModelForm):
    class Meta:
        model=Crisis
        exclude=['isActive','date','time']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

class ReportReceiverForm(forms.ModelForm):
    class Meta:
        model = ReportReceiver
        fields = "__all__"

class CrisisForm(forms.ModelForm):
    class Meta:
        model = Crisis
        fields = ['description','postalcode', 'severity' ]
