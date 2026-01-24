from django import forms
from .models import Load


class LoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = [
            'origem_cidade', 'origem_pais', 'destino_cidade', 'destino_pais',
            'tipo_carga', 'tipo_trailer', 'peso_toneladas', 'distancia_km',
            'pagamento_eur', 'combustivel_litros', 'tempo_viagem',
            'dano_percentual', 'multas', 'status', 'screenshot', 'notas'
        ]
        widgets = {
            'origem_cidade': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Lisboa'}),
            'origem_pais': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Portugal'}),
            'destino_cidade': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Madrid'}),
            'destino_pais': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Espanha'}),
            'tipo_carga': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Madeira'}),
            'tipo_trailer': forms.Select(attrs={'class': 'form-select'}),
            'peso_toneladas': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'distancia_km': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'pagamento_eur': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'combustivel_litros': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'tempo_viagem': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 02:30:00'}),
            'dano_percentual': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'max': '100', 'min': '0'}),
            'multas': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'screenshot': forms.FileInput(attrs={'class': 'form-input'}),
            'notas': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
        }
