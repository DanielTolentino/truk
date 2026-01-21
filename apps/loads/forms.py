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
            'origem_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Lisboa'}),
            'origem_pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Portugal'}),
            'destino_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Madrid'}),
            'destino_pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Espanha'}),
            'tipo_carga': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Madeira'}),
            'tipo_trailer': forms.Select(attrs={'class': 'form-control'}),
            'peso_toneladas': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'distancia_km': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'pagamento_eur': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'combustivel_litros': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tempo_viagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 02:30:00'}),
            'dano_percentual': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'max': '100', 'min': '0'}),
            'multas': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'screenshot': forms.FileInput(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
