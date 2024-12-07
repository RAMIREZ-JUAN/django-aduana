from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre','equipo' ,'unidad', 'marca', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'equipo':forms.Select(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'marca':forms.TextInput(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }