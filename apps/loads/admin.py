from django.contrib import admin
from .models import Load


@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    list_display = ['rota', 'motorista', 'status', 'pagamento_eur', 'distancia_km', 'data_criacao']
    list_filter = ['status', 'tipo_trailer', 'origem_pais', 'destino_pais', 'data_criacao']
    search_fields = ['origem_cidade', 'destino_cidade', 'tipo_carga', 'motorista__username']
    readonly_fields = ['data_criacao', 'data_inicio', 'data_conclusao']
    
    fieldsets = (
        ('Motorista', {
            'fields': ('motorista',)
        }),
        ('Origem e Destino', {
            'fields': ('origem_cidade', 'origem_pais', 'destino_cidade', 'destino_pais')
        }),
        ('Informações da Carga', {
            'fields': ('tipo_carga', 'tipo_trailer', 'peso_toneladas')
        }),
        ('Financeiro', {
            'fields': ('distancia_km', 'pagamento_eur', 'multas')
        }),
        ('Detalhes Técnicos', {
            'fields': ('combustivel_litros', 'tempo_viagem', 'dano_percentual')
        }),
        ('Status e Datas', {
            'fields': ('status', 'data_criacao', 'data_inicio', 'data_conclusao')
        }),
        ('Extras', {
            'fields': ('screenshot', 'notas')
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(deleted_at__isnull=True)
