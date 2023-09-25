from django import forms    

from .models import FinancialRecord,Tag

INPUT_CLASSES =  'form-control py-4 w-76'

class NewFinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = ('tags', 'name', 'description', 'debit', 'credit', 'currency',)
        widgets = {
            'tags': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'debit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'credit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currency': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }), 
        } 

class EditFinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = ('tags', 'name', 'description', 'debit', 'credit', 'currency',)
        widgets = {
            'tags': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'debit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'credit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currency': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }), 
        } 

class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)
        widgets = {
            'tag': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        } 

class EditTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)
        widgets = {
            'tag': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        } 