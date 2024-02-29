from django import forms
from .models import Profile

# Formulario para editar el perfil del usuario
class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=100, required=False)  
    email = forms.EmailField(label='Email', max_length=150, required=False)  

    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'email']