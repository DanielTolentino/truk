from django.db import models
from django.conf import settings
from django.utils import timezone


class Achievement(models.Model):
    """Definição de uma conquista disponível no sistema."""
    
    CATEGORY_CHOICES = [
        ('delivery', 'Entregas'),
        ('distance', 'Distância'),
        ('revenue', 'Receita'),
        ('quality', 'Qualidade'),
        ('exploration', 'Exploração'),
        ('streak', 'Sequência'),
    ]
    
    TIER_CHOICES = [
        ('bronze', 'Bronze'),
        ('silver', 'Prata'),
        ('gold', 'Ouro'),
        ('platinum', 'Platina'),
    ]
    
    code = models.CharField(max_length=50, unique=True, verbose_name='Código')
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    icon = models.CharField(max_length=10, default='🏆', verbose_name='Ícone')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Categoria')
    tier = models.CharField(max_length=20, choices=TIER_CHOICES, default='bronze', verbose_name='Nível')
    
    # Requisitos para desbloquear
    requirement_type = models.CharField(max_length=50, verbose_name='Tipo de Requisito')
    requirement_value = models.IntegerField(verbose_name='Valor Necessário')
    
    # Pontos de XP concedidos
    xp_reward = models.IntegerField(default=100, verbose_name='XP de Recompensa')
    
    # Ordenação e status
    order = models.IntegerField(default=0, verbose_name='Ordem')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name = 'Conquista'
        verbose_name_plural = 'Conquistas'
        ordering = ['category', 'order', 'tier']
    
    def __str__(self):
        return f"{self.icon} {self.name} ({self.get_tier_display()})"


class UserAchievement(models.Model):
    """Registro de conquistas desbloqueadas por usuários."""
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='achievements',
        verbose_name='Usuário'
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Conquista'
    )
    unlocked_at = models.DateTimeField(auto_now_add=True, verbose_name='Desbloqueada em')
    progress_value = models.IntegerField(default=0, verbose_name='Valor de Progresso')
    
    class Meta:
        verbose_name = 'Conquista do Usuário'
        verbose_name_plural = 'Conquistas dos Usuários'
        unique_together = ['user', 'achievement']
        ordering = ['-unlocked_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"
    
    @property
    def progress_percentage(self):
        """Calcula a porcentagem de progresso."""
        if self.achievement.requirement_value == 0:
            return 100
        return min(100, int((self.progress_value / self.achievement.requirement_value) * 100))
    
    @property
    def is_completed(self):
        """Verifica se a conquista foi completada."""
        return self.progress_value >= self.achievement.requirement_value


class UserStats(models.Model):
    """Estatísticas agregadas do usuário para cálculo de conquistas."""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stats',
        verbose_name='Usuário'
    )
    
    # Estatísticas de entregas
    total_deliveries = models.IntegerField(default=0, verbose_name='Total de Entregas')
    successful_deliveries = models.IntegerField(default=0, verbose_name='Entregas Bem-sucedidas')
    perfect_deliveries = models.IntegerField(default=0, verbose_name='Entregas Perfeitas (0% dano)')
    
    # Estatísticas de distância
    total_distance_km = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Distância Total (km)')
    longest_delivery_km = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Maior Entrega (km)')
    
    # Estatísticas financeiras
    total_revenue = models.DecimalField(max_digits=14, decimal_places=2, default=0, verbose_name='Receita Total (€)')
    total_fines = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total de Multas (€)')
    highest_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Maior Pagamento (€)')
    
    # Estatísticas de qualidade
    total_damage_accumulated = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Dano Acumulado (%)')
    average_damage = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Dano Médio (%)')
    deliveries_under_5_damage = models.IntegerField(default=0, verbose_name='Entregas com <5% dano')
    
    # Estatísticas de exploração
    unique_countries_visited = models.IntegerField(default=0, verbose_name='Países Visitados')
    unique_cities_visited = models.IntegerField(default=0, verbose_name='Cidades Visitadas')
    unique_routes = models.IntegerField(default=0, verbose_name='Rotas Únicas')
    
    # Combustível
    total_fuel_consumed = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Combustível Total (L)')
    
    # XP e Nível
    total_xp = models.IntegerField(default=0, verbose_name='XP Total')
    level = models.IntegerField(default=1, verbose_name='Nível')
    
    # Última atualização
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')
    
    class Meta:
        verbose_name = 'Estatísticas do Usuário'
        verbose_name_plural = 'Estatísticas dos Usuários'
    
    def __str__(self):
        return f"Stats: {self.user.username} (Nível {self.level})"
    
    @property
    def xp_for_next_level(self):
        """XP necessário para o próximo nível."""
        return self.level * 1000
    
    @property
    def xp_progress_percentage(self):
        """Progresso percentual para o próximo nível."""
        xp_in_current_level = self.total_xp - ((self.level - 1) * 1000)
        return min(100, int((xp_in_current_level / self.xp_for_next_level) * 100))
    
    @property
    def level_title(self):
        """Título baseado no nível."""
        titles = {
            1: 'Iniciante',
            5: 'Aprendiz',
            10: 'Motorista',
            15: 'Experiente',
            20: 'Profissional',
            25: 'Veterano',
            30: 'Mestre',
            40: 'Lenda',
            50: 'Lenda Suprema',
        }
        for level, title in sorted(titles.items(), reverse=True):
            if self.level >= level:
                return title
        return 'Iniciante'
    
    def add_xp(self, amount):
        """Adiciona XP e verifica se subiu de nível."""
        self.total_xp += amount
        new_level = (self.total_xp // 1000) + 1
        leveled_up = new_level > self.level
        self.level = new_level
        self.save()
        return leveled_up
