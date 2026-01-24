from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils import timezone


class ActiveLoadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class Load(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('falhada', 'Falhada'),
    ]
    
    TRAILER_CHOICES = [
        ('curtain', 'Curtain Side'),
        ('box', 'Box Trailer'),
        ('reefer', 'Refrigerado'),
        ('flatbed', 'Flatbed'),
        ('lowboy', 'Lowboy'),
        ('tanker', 'Tanque'),
        ('container', 'Container'),
        ('log', 'Madeira'),
        ('car_transporter', 'Cegonha'),
    ]
    
    # Relações
    motorista = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='cargas',
        verbose_name='Motorista'
    )
    
    # Informações Básicas
    origem_cidade = models.CharField(max_length=100, verbose_name='Cidade de Origem')
    origem_pais = models.CharField(max_length=100, verbose_name='País de Origem')
    destino_cidade = models.CharField(max_length=100, verbose_name='Cidade de Destino')
    destino_pais = models.CharField(max_length=100, verbose_name='País de Destino')
    tipo_carga = models.CharField(max_length=200, verbose_name='Tipo de Carga')
    distancia_km = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Distância (km)')
    pagamento_eur = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Pagamento (€)')
    
    # Informações Avançadas
    tipo_trailer = models.CharField(
        max_length=50, 
        choices=TRAILER_CHOICES, 
        verbose_name='Tipo de Trailer',
        blank=True,
        null=True
    )
    peso_toneladas = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name='Peso (toneladas)',
        null=True,
        blank=True
    )
    dano_percentual = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name='Dano (%)',
        default=0.00,
        help_text='Dano recebido durante o transporte'
    )
    combustivel_litros = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        verbose_name='Combustível (litros)',
        null=True,
        blank=True
    )
    tempo_viagem = models.DurationField(verbose_name='Tempo de Viagem', null=True, blank=True)
    multas = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Multas (€)',
        default=0.00
    )
    
    # Status e Datas
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pendente',
        verbose_name='Status'
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_inicio = models.DateTimeField(null=True, blank=True, verbose_name='Data de Início')
    data_conclusao = models.DateTimeField(null=True, blank=True, verbose_name='Data de Conclusão')
    
    # Extras
    screenshot = models.ImageField(
        upload_to='screenshots/', 
        null=True, 
        blank=True,
        verbose_name='Screenshot'
    )
    notas = models.TextField(blank=True, null=True, verbose_name='Notas')
    
    # Soft Delete
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deletado em')

    objects = ActiveLoadManager()
    all_objects = models.Manager()
    
    class Meta:
        verbose_name = 'Carga'
        verbose_name_plural = 'Cargas'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"{self.origem_cidade} → {self.destino_cidade} ({self.tipo_carga})"
    
    @property
    def lucro_liquido(self):
        """Calcula o lucro líquido (pagamento - multas)"""
        return self.pagamento_eur - self.multas
    
    @property
    def rota(self):
        """Retorna a rota formatada"""
        return f"{self.origem_cidade}, {self.origem_pais} → {self.destino_cidade}, {self.destino_pais}"
    
    @property
    def eficiencia(self):
        """Calcula eficiência baseada em dano (quanto menos dano, maior eficiência)"""
        return 100 - float(self.dano_percentual)
    
    def soft_delete(self):
        """Marca como deletado ao invés de deletar do banco"""
        self.deleted_at = timezone.now()
        self.save()
    
    def iniciar(self):
        """Marca carga como em andamento"""
        if self.status != 'pendente':
            raise ValidationError('A carga precisa estar pendente para iniciar.')
        self.status = 'em_andamento'
        self.data_inicio = timezone.now()
        self.save()
    
    def concluir(self):
        """Marca carga como concluída"""
        if self.status != 'em_andamento':
            raise ValidationError('A carga precisa estar em andamento para concluir.')
        self.status = 'concluida'
        self.data_conclusao = timezone.now()
        self.save()
    
    def falhar(self):
        """Marca carga como falhada"""
        if self.status != 'em_andamento':
            raise ValidationError('A carga precisa estar em andamento para falhar.')
        self.status = 'falhada'
        self.data_conclusao = timezone.now()
        self.save()
