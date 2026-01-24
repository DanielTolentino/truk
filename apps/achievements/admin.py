from django.contrib import admin
from .models import Achievement, UserAchievement, UserStats


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'category', 'tier', 'requirement_type', 'requirement_value', 'xp_reward', 'is_active']
    list_filter = ['category', 'tier', 'is_active']
    search_fields = ['name', 'code', 'description']
    ordering = ['category', 'order', 'tier']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('code', 'name', 'description', 'icon')
        }),
        ('Classificação', {
            'fields': ('category', 'tier', 'order')
        }),
        ('Requisitos', {
            'fields': ('requirement_type', 'requirement_value')
        }),
        ('Recompensa', {
            'fields': ('xp_reward',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'progress_value', 'progress_percentage', 'is_completed', 'unlocked_at']
    list_filter = ['achievement__category', 'achievement__tier']
    search_fields = ['user__username', 'achievement__name']
    raw_id_fields = ['user', 'achievement']
    readonly_fields = ['unlocked_at']


@admin.register(UserStats)
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'total_xp', 'total_deliveries', 'total_distance_km', 'total_revenue']
    search_fields = ['user__username']
    raw_id_fields = ['user']
    readonly_fields = ['last_updated']
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user',)
        }),
        ('Nível e XP', {
            'fields': ('level', 'total_xp')
        }),
        ('Entregas', {
            'fields': ('total_deliveries', 'successful_deliveries', 'perfect_deliveries')
        }),
        ('Distância', {
            'fields': ('total_distance_km', 'longest_delivery_km')
        }),
        ('Financeiro', {
            'fields': ('total_revenue', 'total_fines', 'highest_payment')
        }),
        ('Qualidade', {
            'fields': ('total_damage_accumulated', 'average_damage', 'deliveries_under_5_damage')
        }),
        ('Exploração', {
            'fields': ('unique_countries_visited', 'unique_cities_visited', 'unique_routes')
        }),
        ('Combustível', {
            'fields': ('total_fuel_consumed',)
        }),
        ('Metadados', {
            'fields': ('last_updated',)
        }),
    )
