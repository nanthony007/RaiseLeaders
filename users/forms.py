from django import forms
from .models import Profile


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', )
    avatar = forms.ChoiceField(widget=forms.RadioSelect(), choices=Profile.AVATARS)

