import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponseNotAllowed, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Load
from .forms import LoadForm, LoadFilterForm


class LoadListView(LoginRequiredMixin, ListView):
    model = Load
    template_name = 'loads/load_list.html'
    context_object_name = 'loads'
    paginate_by = 20
    
    def get_queryset(self):
        qs = Load.objects.select_related('motorista')
        
        # Se não for admin, mostra apenas cargas do motorista
        if not self.request.user.is_admin:
            qs = qs.filter(motorista=self.request.user)
        
        # Filtros
        self.filter_form = LoadFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data.get('status'):
                qs = qs.filter(status=data['status'])
            if data.get('search'):
                search = data['search']
                qs = qs.filter(
                    Q(origem_cidade__icontains=search) |
                    Q(destino_cidade__icontains=search) |
                    Q(tipo_carga__icontains=search) |
                    Q(motorista__username__icontains=search)
                )
            if data.get('tipo_trailer'):
                qs = qs.filter(tipo_trailer=data['tipo_trailer'])
            if data.get('origem_pais'):
                qs = qs.filter(origem_pais__icontains=data['origem_pais'])
            if data.get('destino_pais'):
                qs = qs.filter(destino_pais__icontains=data['destino_pais'])
            if data.get('date_from'):
                qs = qs.filter(data_criacao__date__gte=data['date_from'])
            if data.get('date_to'):
                qs = qs.filter(data_criacao__date__lte=data['date_to'])
            if data.get('min_payment') is not None:
                qs = qs.filter(pagamento_eur__gte=data['min_payment'])
            if data.get('max_payment') is not None:
                qs = qs.filter(pagamento_eur__lte=data['max_payment'])
        
        return qs.order_by('-data_criacao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = getattr(self, 'filter_form', LoadFilterForm())
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['querystring'] = query_params.urlencode()
        return context
    
    def get_template_names(self):
        # Retorna template parcial para requisições HTMX
        if self.request.headers.get('HX-Request'):
            return ['loads/partials/load_table.html']
        return [self.template_name]


class LoadExportCSVView(LoginRequiredMixin, View):
    """Exporta cargas para CSV respeitando os filtros aplicados."""
    
    def get(self, request):
        qs = Load.objects.select_related('motorista')
        
        # Se não for admin, mostra apenas cargas do motorista
        if not request.user.is_admin:
            qs = qs.filter(motorista=request.user)
        
        # Aplica os mesmos filtros da listagem
        filter_form = LoadFilterForm(request.GET)
        if filter_form.is_valid():
            data = filter_form.cleaned_data
            if data.get('status'):
                qs = qs.filter(status=data['status'])
            if data.get('search'):
                search = data['search']
                qs = qs.filter(
                    Q(origem_cidade__icontains=search) |
                    Q(destino_cidade__icontains=search) |
                    Q(tipo_carga__icontains=search) |
                    Q(motorista__username__icontains=search)
                )
            if data.get('tipo_trailer'):
                qs = qs.filter(tipo_trailer=data['tipo_trailer'])
            if data.get('origem_pais'):
                qs = qs.filter(origem_pais__icontains=data['origem_pais'])
            if data.get('destino_pais'):
                qs = qs.filter(destino_pais__icontains=data['destino_pais'])
            if data.get('date_from'):
                qs = qs.filter(data_criacao__date__gte=data['date_from'])
            if data.get('date_to'):
                qs = qs.filter(data_criacao__date__lte=data['date_to'])
            if data.get('min_payment') is not None:
                qs = qs.filter(pagamento_eur__gte=data['min_payment'])
            if data.get('max_payment') is not None:
                qs = qs.filter(pagamento_eur__lte=data['max_payment'])
        
        qs = qs.order_by('-data_criacao')
        
        # Cria resposta CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cargas_truk.csv"'
        response.write('\ufeff')  # BOM para Excel reconhecer UTF-8
        
        writer = csv.writer(response, delimiter=';')
        
        # Cabeçalhos
        writer.writerow([
            'Data',
            'Status',
            'Motorista',
            'Origem (Cidade)',
            'Origem (País)',
            'Destino (Cidade)',
            'Destino (País)',
            'Tipo de Carga',
            'Tipo de Trailer',
            'Distância (km)',
            'Peso (ton)',
            'Pagamento (€)',
            'Multas (€)',
            'Lucro Líquido (€)',
            'Dano (%)',
            'Combustível (L)',
            'Tempo de Viagem',
            'Notas'
        ])
        
        # Dados
        for load in qs:
            writer.writerow([
                load.data_criacao.strftime('%d/%m/%Y %H:%M'),
                load.get_status_display(),
                load.motorista.username,
                load.origem_cidade,
                load.origem_pais,
                load.destino_cidade,
                load.destino_pais,
                load.tipo_carga,
                load.get_tipo_trailer_display() if load.tipo_trailer else '',
                str(load.distancia_km).replace('.', ','),
                str(load.peso_toneladas).replace('.', ',') if load.peso_toneladas else '',
                str(load.pagamento_eur).replace('.', ','),
                str(load.multas).replace('.', ','),
                str(load.lucro_liquido).replace('.', ','),
                str(load.dano_percentual).replace('.', ','),
                str(load.combustivel_litros).replace('.', ',') if load.combustivel_litros else '',
                str(load.tempo_viagem) if load.tempo_viagem else '',
                load.notas or ''
            ])
        
        return response


class LoadDetailView(LoginRequiredMixin, DetailView):
    model = Load
    template_name = 'loads/load_detail.html'
    context_object_name = 'load'
    
    def get_queryset(self):
        qs = Load.objects.select_related('motorista')
        if not self.request.user.is_admin:
            qs = qs.filter(motorista=self.request.user)
        return qs


class LoadCreateView(LoginRequiredMixin, CreateView):
    model = Load
    form_class = LoadForm
    template_name = 'loads/load_form.html'
    success_url = reverse_lazy('loads:list')
    
    def form_valid(self, form):
        form.instance.motorista = self.request.user
        messages.success(self.request, 'Carga registrada com sucesso!')
        return super().form_valid(form)


class LoadUpdateView(LoginRequiredMixin, UpdateView):
    model = Load
    form_class = LoadForm
    template_name = 'loads/load_form.html'
    success_url = reverse_lazy('loads:list')
    
    def get_queryset(self):
        qs = Load.objects.select_related('motorista')
        if not self.request.user.is_admin:
            qs = qs.filter(motorista=self.request.user)
        return qs
    
    def form_valid(self, form):
        messages.success(self.request, 'Carga atualizada com sucesso!')
        return super().form_valid(form)


class LoadDeleteView(LoginRequiredMixin, DeleteView):
    model = Load
    template_name = 'loads/load_confirm_delete.html'
    success_url = reverse_lazy('loads:list')
    
    def get_queryset(self):
        qs = Load.objects.select_related('motorista')
        if not self.request.user.is_admin:
            qs = qs.filter(motorista=self.request.user)
        return qs
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        messages.success(request, 'Carga removida com sucesso!')
        return redirect(self.success_url)


@login_required
def load_status_change(request, pk, action):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    load = get_object_or_404(Load, pk=pk)
    
    # Verifica permissões
    if not request.user.is_admin and load.motorista != request.user:
        messages.error(request, 'Você não tem permissão para alterar esta carga.')
        return redirect('loads:detail', pk=pk)
    
    if action == 'iniciar':
        try:
            load.iniciar()
            messages.success(request, 'Carga iniciada!')
        except Exception as exc:
            messages.error(request, str(exc))
    elif action == 'concluir':
        try:
            load.concluir()
            messages.success(request, 'Carga concluída!')
        except Exception as exc:
            messages.error(request, str(exc))
    elif action == 'falhar':
        try:
            load.falhar()
            messages.warning(request, 'Carga marcada como falhada.')
        except Exception as exc:
            messages.error(request, str(exc))
    else:
        messages.error(request, 'Ação inválida para status da carga.')
    
    return redirect('loads:detail', pk=pk)


@login_required
def load_route_suggestions(request):
    term = request.GET.get('q', '').strip()
    if not term:
        return JsonResponse({'results': []})

    loads = Load.objects.select_related('motorista')
    if not request.user.is_admin:
        loads = loads.filter(motorista=request.user)

    matches = loads.filter(
        Q(origem_cidade__icontains=term) |
        Q(destino_cidade__icontains=term) |
        Q(origem_pais__icontains=term) |
        Q(destino_pais__icontains=term)
    ).values('origem_cidade', 'origem_pais', 'destino_cidade', 'destino_pais')

    results = []
    seen = set()
    for item in matches[:20]:
        key = (
            item['origem_cidade'],
            item['origem_pais'],
            item['destino_cidade'],
            item['destino_pais']
        )
        if key in seen:
            continue
        seen.add(key)
        results.append({
            'label': f"{item['origem_cidade']}, {item['origem_pais']} → {item['destino_cidade']}, {item['destino_pais']}",
            'value': item['origem_cidade']
        })

    return JsonResponse({'results': results})
