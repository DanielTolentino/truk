from django.db import migrations


def create_initial_achievements(apps, schema_editor):
    """Cria as conquistas iniciais do sistema."""
    Achievement = apps.get_model('achievements', 'Achievement')
    
    achievements = [
        # Entregas - Bronze
        {
            'code': 'first_delivery',
            'name': 'Primeira Entrega',
            'description': 'Complete sua primeira entrega com sucesso.',
            'icon': '🚚',
            'category': 'delivery',
            'tier': 'bronze',
            'requirement_type': 'total_deliveries',
            'requirement_value': 1,
            'xp_reward': 50,
            'order': 1,
        },
        {
            'code': 'delivery_10',
            'name': 'Motorista Iniciante',
            'description': 'Complete 10 entregas com sucesso.',
            'icon': '📦',
            'category': 'delivery',
            'tier': 'bronze',
            'requirement_type': 'total_deliveries',
            'requirement_value': 10,
            'xp_reward': 100,
            'order': 2,
        },
        # Entregas - Silver
        {
            'code': 'delivery_50',
            'name': 'Motorista Experiente',
            'description': 'Complete 50 entregas com sucesso.',
            'icon': '🚛',
            'category': 'delivery',
            'tier': 'silver',
            'requirement_type': 'total_deliveries',
            'requirement_value': 50,
            'xp_reward': 250,
            'order': 3,
        },
        # Entregas - Gold
        {
            'code': 'delivery_100',
            'name': 'Veterano das Estradas',
            'description': 'Complete 100 entregas com sucesso.',
            'icon': '🏅',
            'category': 'delivery',
            'tier': 'gold',
            'requirement_type': 'total_deliveries',
            'requirement_value': 100,
            'xp_reward': 500,
            'order': 4,
        },
        # Entregas - Platinum
        {
            'code': 'delivery_500',
            'name': 'Lenda do Asfalto',
            'description': 'Complete 500 entregas com sucesso.',
            'icon': '👑',
            'category': 'delivery',
            'tier': 'platinum',
            'requirement_type': 'total_deliveries',
            'requirement_value': 500,
            'xp_reward': 1000,
            'order': 5,
        },
        
        # Distância - Bronze
        {
            'code': 'distance_1000',
            'name': 'Primeiro Milhar',
            'description': 'Percorra 1.000 km no total.',
            'icon': '🛣️',
            'category': 'distance',
            'tier': 'bronze',
            'requirement_type': 'total_distance_km',
            'requirement_value': 1000,
            'xp_reward': 100,
            'order': 1,
        },
        # Distância - Silver
        {
            'code': 'distance_10000',
            'name': 'Maratonista',
            'description': 'Percorra 10.000 km no total.',
            'icon': '🗺️',
            'category': 'distance',
            'tier': 'silver',
            'requirement_type': 'total_distance_km',
            'requirement_value': 10000,
            'xp_reward': 300,
            'order': 2,
        },
        # Distância - Gold
        {
            'code': 'distance_50000',
            'name': 'Atravessador de Continentes',
            'description': 'Percorra 50.000 km no total.',
            'icon': '🌍',
            'category': 'distance',
            'tier': 'gold',
            'requirement_type': 'total_distance_km',
            'requirement_value': 50000,
            'xp_reward': 750,
            'order': 3,
        },
        # Distância - Platinum
        {
            'code': 'distance_100000',
            'name': 'Volta ao Mundo',
            'description': 'Percorra 100.000 km no total.',
            'icon': '🌐',
            'category': 'distance',
            'tier': 'platinum',
            'requirement_type': 'total_distance_km',
            'requirement_value': 100000,
            'xp_reward': 1500,
            'order': 4,
        },
        
        # Receita - Bronze
        {
            'code': 'revenue_10000',
            'name': 'Primeiros Lucros',
            'description': 'Acumule €10.000 em pagamentos.',
            'icon': '💵',
            'category': 'revenue',
            'tier': 'bronze',
            'requirement_type': 'total_revenue',
            'requirement_value': 10000,
            'xp_reward': 100,
            'order': 1,
        },
        # Receita - Silver
        {
            'code': 'revenue_100000',
            'name': 'Empresário',
            'description': 'Acumule €100.000 em pagamentos.',
            'icon': '💰',
            'category': 'revenue',
            'tier': 'silver',
            'requirement_type': 'total_revenue',
            'requirement_value': 100000,
            'xp_reward': 400,
            'order': 2,
        },
        # Receita - Gold
        {
            'code': 'revenue_500000',
            'name': 'Magnata',
            'description': 'Acumule €500.000 em pagamentos.',
            'icon': '🤑',
            'category': 'revenue',
            'tier': 'gold',
            'requirement_type': 'total_revenue',
            'requirement_value': 500000,
            'xp_reward': 800,
            'order': 3,
        },
        # Receita - Platinum
        {
            'code': 'revenue_1000000',
            'name': 'Milionário',
            'description': 'Acumule €1.000.000 em pagamentos.',
            'icon': '💎',
            'category': 'revenue',
            'tier': 'platinum',
            'requirement_type': 'total_revenue',
            'requirement_value': 1000000,
            'xp_reward': 2000,
            'order': 4,
        },
        
        # Qualidade - Bronze
        {
            'code': 'perfect_1',
            'name': 'Entrega Perfeita',
            'description': 'Complete uma entrega com 0% de dano.',
            'icon': '✨',
            'category': 'quality',
            'tier': 'bronze',
            'requirement_type': 'perfect_deliveries',
            'requirement_value': 1,
            'xp_reward': 75,
            'order': 1,
        },
        # Qualidade - Silver
        {
            'code': 'perfect_10',
            'name': 'Mãos de Ouro',
            'description': 'Complete 10 entregas com 0% de dano.',
            'icon': '🌟',
            'category': 'quality',
            'tier': 'silver',
            'requirement_type': 'perfect_deliveries',
            'requirement_value': 10,
            'xp_reward': 300,
            'order': 2,
        },
        # Qualidade - Gold
        {
            'code': 'perfect_50',
            'name': 'Perfecionista',
            'description': 'Complete 50 entregas com 0% de dano.',
            'icon': '⭐',
            'category': 'quality',
            'tier': 'gold',
            'requirement_type': 'perfect_deliveries',
            'requirement_value': 50,
            'xp_reward': 750,
            'order': 3,
        },
        # Qualidade - Platinum
        {
            'code': 'perfect_100',
            'name': 'Intocável',
            'description': 'Complete 100 entregas com 0% de dano.',
            'icon': '💫',
            'category': 'quality',
            'tier': 'platinum',
            'requirement_type': 'perfect_deliveries',
            'requirement_value': 100,
            'xp_reward': 1500,
            'order': 4,
        },
        {
            'code': 'low_damage_25',
            'name': 'Cuidadoso',
            'description': 'Complete 25 entregas com menos de 5% de dano.',
            'icon': '🛡️',
            'category': 'quality',
            'tier': 'silver',
            'requirement_type': 'deliveries_under_5_damage',
            'requirement_value': 25,
            'xp_reward': 200,
            'order': 5,
        },
        
        # Exploração - Bronze
        {
            'code': 'countries_5',
            'name': 'Turista',
            'description': 'Visite 5 países diferentes.',
            'icon': '🗺️',
            'category': 'exploration',
            'tier': 'bronze',
            'requirement_type': 'unique_countries_visited',
            'requirement_value': 5,
            'xp_reward': 150,
            'order': 1,
        },
        # Exploração - Silver
        {
            'code': 'countries_10',
            'name': 'Explorador',
            'description': 'Visite 10 países diferentes.',
            'icon': '🧭',
            'category': 'exploration',
            'tier': 'silver',
            'requirement_type': 'unique_countries_visited',
            'requirement_value': 10,
            'xp_reward': 350,
            'order': 2,
        },
        # Exploração - Gold
        {
            'code': 'countries_15',
            'name': 'Globetrotter',
            'description': 'Visite 15 países diferentes.',
            'icon': '🌍',
            'category': 'exploration',
            'tier': 'gold',
            'requirement_type': 'unique_countries_visited',
            'requirement_value': 15,
            'xp_reward': 600,
            'order': 3,
        },
        # Exploração - Cidades
        {
            'code': 'cities_20',
            'name': 'Conhecedor de Cidades',
            'description': 'Visite 20 cidades diferentes.',
            'icon': '🏙️',
            'category': 'exploration',
            'tier': 'silver',
            'requirement_type': 'unique_cities_visited',
            'requirement_value': 20,
            'xp_reward': 300,
            'order': 4,
        },
        {
            'code': 'cities_50',
            'name': 'Cartógrafo',
            'description': 'Visite 50 cidades diferentes.',
            'icon': '📍',
            'category': 'exploration',
            'tier': 'gold',
            'requirement_type': 'unique_cities_visited',
            'requirement_value': 50,
            'xp_reward': 700,
            'order': 5,
        },
        # Exploração - Rotas
        {
            'code': 'routes_10',
            'name': 'Diversificador',
            'description': 'Complete 10 rotas únicas.',
            'icon': '🛤️',
            'category': 'exploration',
            'tier': 'bronze',
            'requirement_type': 'unique_routes',
            'requirement_value': 10,
            'xp_reward': 150,
            'order': 6,
        },
        {
            'code': 'routes_50',
            'name': 'Mestre das Rotas',
            'description': 'Complete 50 rotas únicas.',
            'icon': '🗺️',
            'category': 'exploration',
            'tier': 'gold',
            'requirement_type': 'unique_routes',
            'requirement_value': 50,
            'xp_reward': 500,
            'order': 7,
        },
    ]
    
    for achievement_data in achievements:
        Achievement.objects.create(**achievement_data)


def reverse_achievements(apps, schema_editor):
    """Remove todas as conquistas."""
    Achievement = apps.get_model('achievements', 'Achievement')
    Achievement.objects.all().delete()


class Migration(migrations.Migration):
    
    dependencies = [
        ('achievements', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(create_initial_achievements, reverse_achievements),
    ]
