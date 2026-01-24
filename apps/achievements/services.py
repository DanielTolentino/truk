from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, Count, Avg, F
from django.db import transaction

from apps.loads.models import Load
from .models import Achievement, UserAchievement, UserStats


def get_or_create_user_stats(user):
    """Obtém ou cria as estatísticas do usuário."""
    stats, created = UserStats.objects.get_or_create(user=user)
    return stats


def update_user_stats(user):
    """Atualiza todas as estatísticas do usuário baseado nas cargas."""
    stats = get_or_create_user_stats(user)
    
    # Busca todas as cargas concluídas do usuário
    loads = Load.objects.filter(motorista=user, status='concluida')
    
    # Estatísticas de entregas
    stats.total_deliveries = loads.count()
    stats.successful_deliveries = loads.count()
    stats.perfect_deliveries = loads.filter(dano_percentual=0).count()
    
    # Estatísticas de distância
    distance_agg = loads.aggregate(
        total=Sum('distancia_km'),
        max_dist=models.Max('distancia_km')
    )
    stats.total_distance_km = distance_agg['total'] or 0
    stats.longest_delivery_km = distance_agg['max_dist'] or 0
    
    # Estatísticas financeiras
    financial_agg = loads.aggregate(
        total_rev=Sum('pagamento_eur'),
        total_fines=Sum('multas'),
        max_payment=models.Max('pagamento_eur')
    )
    stats.total_revenue = financial_agg['total_rev'] or 0
    stats.total_fines = financial_agg['total_fines'] or 0
    stats.highest_payment = financial_agg['max_payment'] or 0
    
    # Estatísticas de qualidade
    quality_agg = loads.aggregate(
        total_damage=Sum('dano_percentual'),
        avg_damage=Avg('dano_percentual')
    )
    stats.total_damage_accumulated = quality_agg['total_damage'] or 0
    stats.average_damage = quality_agg['avg_damage'] or 0
    stats.deliveries_under_5_damage = loads.filter(dano_percentual__lt=5).count()
    
    # Estatísticas de exploração
    countries = set()
    cities = set()
    routes = set()
    
    for load in loads:
        countries.add(load.origem_pais)
        countries.add(load.destino_pais)
        cities.add(f"{load.origem_cidade}, {load.origem_pais}")
        cities.add(f"{load.destino_cidade}, {load.destino_pais}")
        routes.add(load.rota)
    
    stats.unique_countries_visited = len(countries)
    stats.unique_cities_visited = len(cities)
    stats.unique_routes = len(routes)
    
    # Combustível
    fuel_total = loads.aggregate(total=Sum('combustivel_litros'))['total']
    stats.total_fuel_consumed = fuel_total or 0
    
    stats.save()
    return stats


def check_achievements(user):
    """Verifica e desbloqueia conquistas para o usuário."""
    stats = get_or_create_user_stats(user)
    update_user_stats(user)
    
    # Recarrega stats após atualização
    stats.refresh_from_db()
    
    achievements = Achievement.objects.filter(is_active=True)
    newly_unlocked = []
    
    for achievement in achievements:
        # Verifica se já tem essa conquista
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=user,
            achievement=achievement,
            defaults={'progress_value': 0}
        )
        
        # Calcula o progresso atual
        current_value = get_achievement_progress(stats, achievement)
        user_achievement.progress_value = current_value
        
        # Verifica se completou
        was_completed = user_achievement.is_completed
        user_achievement.save()
        
        if not was_completed and user_achievement.is_completed:
            # Acabou de completar!
            newly_unlocked.append(achievement)
            stats.add_xp(achievement.xp_reward)
    
    return newly_unlocked


def get_achievement_progress(stats, achievement):
    """Retorna o valor atual de progresso para uma conquista."""
    requirement_type = achievement.requirement_type
    
    progress_mapping = {
        'total_deliveries': stats.total_deliveries,
        'successful_deliveries': stats.successful_deliveries,
        'perfect_deliveries': stats.perfect_deliveries,
        'total_distance_km': int(stats.total_distance_km),
        'longest_delivery_km': int(stats.longest_delivery_km),
        'total_revenue': int(stats.total_revenue),
        'highest_payment': int(stats.highest_payment),
        'deliveries_under_5_damage': stats.deliveries_under_5_damage,
        'unique_countries_visited': stats.unique_countries_visited,
        'unique_cities_visited': stats.unique_cities_visited,
        'unique_routes': stats.unique_routes,
        'total_fuel_consumed': int(stats.total_fuel_consumed),
        'level': stats.level,
    }
    
    return progress_mapping.get(requirement_type, 0)


@receiver(post_save, sender=Load)
def on_load_saved(sender, instance, **kwargs):
    """Quando uma carga é salva, verifica conquistas."""
    if instance.status == 'concluida':
        # Atualiza stats e verifica conquistas
        check_achievements(instance.motorista)


# Importação necessária para signals funcionarem
from django.db import models
