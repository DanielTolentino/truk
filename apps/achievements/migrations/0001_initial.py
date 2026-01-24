# Generated migration for achievements app

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('icon', models.CharField(default='🏆', max_length=10, verbose_name='Ícone')),
                ('category', models.CharField(choices=[('delivery', 'Entregas'), ('distance', 'Distância'), ('revenue', 'Receita'), ('quality', 'Qualidade'), ('exploration', 'Exploração'), ('streak', 'Sequência')], max_length=20, verbose_name='Categoria')),
                ('tier', models.CharField(choices=[('bronze', 'Bronze'), ('silver', 'Prata'), ('gold', 'Ouro'), ('platinum', 'Platina')], default='bronze', max_length=20, verbose_name='Nível')),
                ('requirement_type', models.CharField(max_length=50, verbose_name='Tipo de Requisito')),
                ('requirement_value', models.IntegerField(verbose_name='Valor Necessário')),
                ('xp_reward', models.IntegerField(default=100, verbose_name='XP de Recompensa')),
                ('order', models.IntegerField(default=0, verbose_name='Ordem')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Conquista',
                'verbose_name_plural': 'Conquistas',
                'ordering': ['category', 'order', 'tier'],
            },
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deliveries', models.IntegerField(default=0, verbose_name='Total de Entregas')),
                ('successful_deliveries', models.IntegerField(default=0, verbose_name='Entregas Bem-sucedidas')),
                ('perfect_deliveries', models.IntegerField(default=0, verbose_name='Entregas Perfeitas (0% dano)')),
                ('total_distance_km', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Distância Total (km)')),
                ('longest_delivery_km', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Maior Entrega (km)')),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=14, verbose_name='Receita Total (€)')),
                ('total_fines', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Total de Multas (€)')),
                ('highest_payment', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Maior Pagamento (€)')),
                ('total_damage_accumulated', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Dano Acumulado (%)')),
                ('average_damage', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dano Médio (%)')),
                ('deliveries_under_5_damage', models.IntegerField(default=0, verbose_name='Entregas com <5% dano')),
                ('unique_countries_visited', models.IntegerField(default=0, verbose_name='Países Visitados')),
                ('unique_cities_visited', models.IntegerField(default=0, verbose_name='Cidades Visitadas')),
                ('unique_routes', models.IntegerField(default=0, verbose_name='Rotas Únicas')),
                ('total_fuel_consumed', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Combustível Total (L)')),
                ('total_xp', models.IntegerField(default=0, verbose_name='XP Total')),
                ('level', models.IntegerField(default=1, verbose_name='Nível')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Estatísticas do Usuário',
                'verbose_name_plural': 'Estatísticas dos Usuários',
            },
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlocked_at', models.DateTimeField(auto_now_add=True, verbose_name='Desbloqueada em')),
                ('progress_value', models.IntegerField(default=0, verbose_name='Valor de Progresso')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='achievements.achievement', verbose_name='Conquista')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Conquista do Usuário',
                'verbose_name_plural': 'Conquistas dos Usuários',
                'ordering': ['-unlocked_at'],
                'unique_together': {('user', 'achievement')},
            },
        ),
    ]
