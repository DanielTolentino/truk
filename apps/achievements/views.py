from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Achievement, UserAchievement, UserStats
from .services import get_or_create_user_stats, update_user_stats


class AchievementsView(LoginRequiredMixin, TemplateView):
    """Página de conquistas do usuário."""
    template_name = 'achievements/achievements.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Atualiza estatísticas
        stats = get_or_create_user_stats(user)
        update_user_stats(user)
        stats.refresh_from_db()
        
        # Busca todas as conquistas
        achievements = Achievement.objects.filter(is_active=True)
        
        # Organiza conquistas por categoria com progresso do usuário
        achievements_by_category = {}
        for achievement in achievements:
            category = achievement.get_category_display()
            if category not in achievements_by_category:
                achievements_by_category[category] = []
            
            # Busca progresso do usuário
            user_achievement = UserAchievement.objects.filter(
                user=user,
                achievement=achievement
            ).first()
            
            achievements_by_category[category].append({
                'achievement': achievement,
                'user_achievement': user_achievement,
                'progress': user_achievement.progress_percentage if user_achievement else 0,
                'is_completed': user_achievement.is_completed if user_achievement else False,
                'progress_value': user_achievement.progress_value if user_achievement else 0,
            })
        
        # Conquistas recentes desbloqueadas
        recent_unlocked = UserAchievement.objects.filter(
            user=user,
            progress_value__gte=models.F('achievement__requirement_value')
        ).select_related('achievement').order_by('-unlocked_at')[:5]
        
        # Estatísticas gerais
        total_achievements = achievements.count()
        completed_achievements = UserAchievement.objects.filter(
            user=user,
            progress_value__gte=models.F('achievement__requirement_value')
        ).count()
        
        context.update({
            'stats': stats,
            'achievements_by_category': achievements_by_category,
            'recent_unlocked': recent_unlocked,
            'total_achievements': total_achievements,
            'completed_achievements': completed_achievements,
            'completion_percentage': int((completed_achievements / total_achievements * 100)) if total_achievements > 0 else 0,
        })
        
        return context


# Importação necessária
from django.db import models
