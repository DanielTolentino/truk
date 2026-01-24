from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
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
