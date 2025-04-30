# inscription/forms.py
from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ['nom', 'prenoms', 'date_naissance', 'lieu_naissance', 
                  'email', 'telephone', 'filiere', 'cni', 'diplome', 'photo']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }