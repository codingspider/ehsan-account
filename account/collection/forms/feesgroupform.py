from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class AddFeesGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddFeesGroupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = FeeGroups
        fields = '__all__'
        widgets = {
                'note': forms.Textarea(attrs={'rows': 5}),
        }


class EditFeesGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditFeesGroupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = FeeGroups
        fields = '__all__'
        exclude = ('active_status',)
        widgets = {
                'note': forms.Textarea(attrs={'rows': 5}),
        }
