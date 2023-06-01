from django import forms

from places.models import Memory


class MemoryForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Memory
        fields = ['name', 'comment', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 500px; margin-bottom: 5px;'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 500px; height: 250px; margin-bottom: 20px;'
            }),
        }
