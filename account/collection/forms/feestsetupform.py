from django import forms
from ..models import *


class FeesGroupFeeTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeesGroupFeeTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeesGroupFeeType
        fields = '__all__'
        exclude = ('active_status',)
