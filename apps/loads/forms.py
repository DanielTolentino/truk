from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Load


class LoadFilterForm(forms.Form):
    search = forms.CharField(required=False)
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os Status')] + Load.STATUS_CHOICES
    )
    tipo_trailer = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os Trailers')] + Load.TRAILER_CHOICES
    )
    origem_pais = forms.CharField(required=False)
    destino_pais = forms.CharField(required=False)
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    min_payment = forms.DecimalField(required=False, min_value=0)
    max_payment = forms.DecimalField(required=False, min_value=0)


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

    def clean_dano_percentual(self):
        value = self.cleaned_data.get('dano_percentual')
        if value is None:
            return value
        if value < 0 or value > 100:
            raise ValidationError('O dano percentual deve estar entre 0 e 100.')
        return value

    def clean_distancia_km(self):
        value = self.cleaned_data.get('distancia_km')
        if value is None:
            return value
        if value < 0:
            raise ValidationError('A distância não pode ser negativa.')
        return value

    def clean_pagamento_eur(self):
        value = self.cleaned_data.get('pagamento_eur')
        if value is None:
            return value
        if value < 0:
            raise ValidationError('O pagamento não pode ser negativo.')
        return value

    def clean_peso_toneladas(self):
        value = self.cleaned_data.get('peso_toneladas')
        if value is None:
            return value
        if value < 0:
            raise ValidationError('O peso não pode ser negativo.')
        return value

    def clean_combustivel_litros(self):
        value = self.cleaned_data.get('combustivel_litros')
        if value is None:
            return value
        if value < 0:
            raise ValidationError('O combustível não pode ser negativo.')
        return value

    def clean_multas(self):
        value = self.cleaned_data.get('multas')
        if value is None:
            return value
        if value < 0:
            raise ValidationError('As multas não podem ser negativas.')
        return value

    def clean_screenshot(self):
        screenshot = self.cleaned_data.get('screenshot')
        if not screenshot:
            return screenshot
        if screenshot.size > 5 * 1024 * 1024:
            raise ValidationError('A imagem deve ter no máximo 5MB.')
        if hasattr(screenshot, 'content_type') and not screenshot.content_type.startswith('image/'):
            raise ValidationError('O screenshot precisa ser uma imagem.')
        return screenshot

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.status == 'em_andamento' and not instance.data_inicio:
            instance.data_inicio = timezone.now()
        if instance.status in ['concluida', 'falhada'] and not instance.data_conclusao:
            instance.data_conclusao = timezone.now()
        if commit:
            instance.save()
            self.save_m2m()
        return instance
