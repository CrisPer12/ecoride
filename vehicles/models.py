# vehicles/models.py
from django.db import models

class Veiculo(models.Model):
    MARCAS = [
        ('FIAT', 'Fiat'),
        ('FORD', 'Ford'),
        # Adicione mais marcas conforme necessário
    ]
    TIPOS_COMBUSTIVEL = [
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('DIESEL', 'Diesel'),
        ('ELETRICO', 'Elétrico'),
        ('HÍBRIDO', 'Híbrido'),
        # Outros tipos
    ]
    CATEGORIAS = [
        ('HATCH', 'Hatch'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('PICAPE', 'Picape'),
        ('MINIVAN', 'MiniVan'),
        # Outras categorias
    ]

    marca = models.CharField(max_length=50, choices=MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    tipo_combustivel = models.CharField(max_length=20, choices=TIPOS_COMBUSTIVEL)
    consumo_urbano = models.FloatField(help_text="km/l ou km/kWh")
    consumo_rodoviario = models.FloatField(help_text="km/l ou km/kWh")
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    capacidade_tanque_bateria = models.FloatField(help_text="Litros ou kWh")
    autonomia_estimada = models.FloatField(help_text="km")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    passageiros = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='veiculos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}"

class Simulacao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='simulacoes')
    periodo_locacao = models.PositiveIntegerField(help_text="Dias")
    distancia_estimada = models.FloatField(help_text="km")
    preco_combustivel = models.DecimalField(max_digits=6, decimal_places=2)
    custo_total_locacao = models.DecimalField(max_digits=10, decimal_places=2)
    custo_estimado_combustivel = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total_projetado = models.DecimalField(max_digits=10, decimal_places=2)
    abastecimentos_estimados = models.PositiveIntegerField()
    data_simulacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulação {self.id} - {self.veiculo}"