from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre', 'unidad', 'marca', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'marca':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }


class ScanForm(forms.ModelForm):
    class Meta:
        model=Task
        fields =['nombre', 'unidad', 'marcas', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'marcas':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }

class CpuForm(forms.ModelForm):
    class Meta:
        model=Task
        fields =['nombre', 'unidad', 'cpu', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'cpu':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }

class MonForm(forms.ModelForm):
    class Meta:
        model=Task
        fields =['nombre', 'unidad', 'modelo', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'modelo':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }    

class LapForm(forms.ModelForm):
    class Meta:
        model=Task
        fields =['nombre', 'unidad', 'model', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'model':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }

class DiskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields =['nombre', 'unidad', 'tipo', 'codigo']
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'tipo':forms.Select(attrs={'class': 'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'})
        }

