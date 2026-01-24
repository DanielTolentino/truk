from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum, Avg, Count, Q
from django.utils import timezone
from datetime import timedelta
from apps.loads.models import Load
import json


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Query base
        if user.is_admin:
            loads = Load.objects.select_related('motorista')
        else:
            loads = Load.objects.select_related('motorista').filter(motorista=user)
        
        # Estatísticas gerais
        total_loads = loads.count()
        completed_loads = loads.filter(status='concluida').count()
        failed_loads = loads.filter(status='falhada').count()
        completed_loads_qs = loads.filter(status='concluida')
        
        stats = completed_loads_qs.aggregate(
            total_km=Sum('distancia_km'),
            total_revenue=Sum('pagamento_eur'),
            total_fines=Sum('multas'),
            avg_damage=Avg('dano_percentual'),
            total_fuel=Sum('combustivel_litros')
        )
        
        # Cargas recentes
        recent_loads = loads.order_by('-data_criacao')[:5]
        
        # Cargas em andamento
        active_loads = loads.filter(status='em_andamento')
        
        # Top rotas (mais utilizadas)
        top_routes = completed_loads_qs.values(
            'origem_cidade', 'destino_cidade'
        ).annotate(
            count=Count('id'),
            total_revenue=Sum('pagamento_eur')
        ).order_by('-count')[:5]
        
        # Dados para gráfico de cargas por mês (últimos 6 meses)
        months_data = []
        for i in range(5, -1, -1):
            date = timezone.now() - timedelta(days=30*i)
            month_loads = loads.filter(
                data_criacao__year=date.year,
                data_criacao__month=date.month
            ).count()
            months_data.append({
                'month': date.strftime('%b %Y'),
                'count': month_loads
            })
        
        # Status distribution
        status_data = loads.values('status').annotate(count=Count('id'))
        
        context.update({
            'total_loads': total_loads,
            'completed_loads': completed_loads,
            'failed_loads': failed_loads,
            'active_loads_count': active_loads.count(),
            'total_km': stats['total_km'] or 0,
            'total_revenue': stats['total_revenue'] or 0,
            'total_fines': stats['total_fines'] or 0,
            'net_revenue': (stats['total_revenue'] or 0) - (stats['total_fines'] or 0),
            'avg_damage': round(stats['avg_damage'] or 0, 2),
            'total_fuel': stats['total_fuel'] or 0,
            'recent_loads': recent_loads,
            'active_loads': active_loads,
            'top_routes': top_routes,
            'months_data': json.dumps(months_data),
            'status_data': json.dumps(list(status_data)),
        })
        
        return context


class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/analytics.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Query base
        if user.is_admin:
            loads = Load.objects.select_related('motorista')
        else:
            loads = Load.objects.select_related('motorista').filter(motorista=user)
        
        # Análise por tipo de trailer
        completed_loads_qs = loads.filter(status='concluida')

        trailer_analysis = list(completed_loads_qs.values('tipo_trailer').annotate(
            count=Count('id'),
            total_revenue=Sum('pagamento_eur'),
            avg_damage=Avg('dano_percentual')
        ).order_by('-count'))

        trailer_display_map = dict(Load.TRAILER_CHOICES)
        for item in trailer_analysis:
            item['tipo_trailer_display'] = trailer_display_map.get(item['tipo_trailer'], 'N/A')
        
        # Análise por país de origem
        origin_analysis = completed_loads_qs.values('origem_pais').annotate(
            count=Count('id'),
            total_revenue=Sum('pagamento_eur')
        ).order_by('-count')[:10]
        
        # Análise por país de destino
        destination_analysis = completed_loads_qs.values('destino_pais').annotate(
            count=Count('id'),
            total_revenue=Sum('pagamento_eur')
        ).order_by('-count')[:10]
        
        # Performance por motorista (apenas para admin)
        if user.is_admin:
            driver_performance = completed_loads_qs.values(
                'motorista__username'
            ).annotate(
                count=Count('id'),
                total_revenue=Sum('pagamento_eur'),
                avg_damage=Avg('dano_percentual')
            ).order_by('-count')
        else:
            driver_performance = None
        
        # Evolução da receita (últimos 12 meses)
        revenue_evolution = []
        for i in range(11, -1, -1):
            date = timezone.now() - timedelta(days=30*i)
            month_revenue = completed_loads_qs.filter(
                data_conclusao__year=date.year,
                data_conclusao__month=date.month
            ).aggregate(total=Sum('pagamento_eur'))['total'] or 0
            revenue_evolution.append({
                'month': date.strftime('%b %Y'),
                'revenue': float(month_revenue)
            })
        
        context.update({
            'trailer_analysis': trailer_analysis,
            'origin_analysis': origin_analysis,
            'destination_analysis': destination_analysis,
            'driver_performance': driver_performance,
            'revenue_evolution': json.dumps(revenue_evolution),
        })
        
        return context
