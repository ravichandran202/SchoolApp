from .models import Announcement
from django import forms
from django.forms import ModelForm

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ('image','title','content','announce_to')
        help_texts = {'announce_to':"Please select 0 - 5 (0 indicates Announce to everybody)"}

