from django import forms

from .models import Group


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields =  ('group_name',)
        widgets = {
            'group_name': forms.TextInput(attrs={
                'class': 'form-control py-4 w-76',
                'regex':r'^[\u4e00-\u9fa5]{4,16}$',
            })
        }
    

class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields =  ('group_name','weight',)
        widgets = {
            'group_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }