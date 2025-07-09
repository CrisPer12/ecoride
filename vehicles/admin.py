# vehicles/admin.py
from django.contrib import admin
from .models import Veiculo, Simulacao

# --- Registro do Modelo Veiculo ---
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = (
        'marca', 'modelo', 'ano', 'tipo_combustivel', 'valor_diaria',
        'autonomia_estimada', 'categoria', 'passageiros'
    )

    list_filter = (
        'tipo_combustivel', 'categoria', 'marca', 'ano'
    )

    search_fields = (
        'marca', 'modelo', 'ano', 'tipo_combustivel' # Permite busca por esses campos
    )

    list_display_links = (
        'marca', 'modelo'
    )

    ordering = ('marca', 'modelo', 'ano',)

    fieldsets = (
        (None, {
            'fields': ('marca', 'modelo', 'ano', 'tipo_combustivel', 'categoria', 'passageiros', 'imagem')
        }),
        ('Detalhes de Consumo e Custo', {
            'fields': ('consumo_urbano', 'consumo_rodoviario', 'valor_diaria', 'capacidade_tanque_bateria', 'autonomia_estimada'),
            'description': 'Informações cruciais para a simulação de performance.'
        }),
    )

# --- Registro do Modelo Simulacao ---
@admin.register(Simulacao)
class SimulacaoAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista de simulações
    list_display = (
        'veiculo', 'periodo_locacao', 'distancia_estimada', 'preco_combustivel',
        'custo_total_locacao', 'custo_estimado_combustivel', 'custo_total_projetado',
        'abastecimentos_estimados', 'data_simulacao'
    )

    list_filter = (
        'veiculo__marca', # Permite filtrar pela marca do veículo relacionado
        'veiculo__tipo_combustivel', # Pelo tipo de combustível do veículo
        'periodo_locacao',
        'data_simulacao'
    )

    search_fields = (
        'veiculo__marca', 'veiculo__modelo', # Permite busca pelo veículo relacionado
        'periodo_locacao'
    )

    ordering = ('-data_simulacao',) # Ordena da mais recente para a mais antiga

    readonly_fields = (
        'custo_total_locacao', 'custo_estimado_combustivel',
        'custo_total_projetado', 'abastecimentos_estimados', 'data_simulacao'
    )

    raw_id_fields = ('veiculo',) # Melhor para muitos veículos, pois usa um pop-up de busca