from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import Load
from .forms import LoadForm


class LoadListView(LoginRequiredMixin, ListView):
    model = Load
    template_name = 'loads/load_list.html'
    context_object_name = 'loads'
    paginate_by = 20
    
    def get_queryset(self):
        qs = Load.objects.filter(deleted_at__isnull=True)
        
        # Se não for admin, mostra apenas cargas do motorista
        if not self.request.user.is_admin:
            qs = qs.filter(motorista=self.request.user)
        
        # Filtros
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(
                Q(origem_cidade__icontains=search) |
                Q(destino_cidade__icontains=search) |
                Q(tipo_carga__icontains=search) |
                Q(motorista__username__icontains=search)
            )
        
        return qs.order_by('-data_criacao')


class LoadDetailView(LoginRequiredMixin, DetailView):
    model = Load
    template_name = 'loads/load_detail.html'
    context_object_name = 'load'
    
    def get_queryset(self):
        qs = Load.objects.filter(deleted_at__isnull=True)
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
        qs = Load.objects.filter(deleted_at__isnull=True)
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
        qs = Load.objects.filter(deleted_at__isnull=True)
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
    load = get_object_or_404(Load, pk=pk, deleted_at__isnull=True)
    
    # Verifica permissões
    if not request.user.is_admin and load.motorista != request.user:
        messages.error(request, 'Você não tem permissão para alterar esta carga.')
        return redirect('loads:detail', pk=pk)
    
    if action == 'iniciar':
        load.iniciar()
        messages.success(request, 'Carga iniciada!')
    elif action == 'concluir':
        load.concluir()
        messages.success(request, 'Carga concluída!')
    elif action == 'falhar':
        load.falhar()
        messages.warning(request, 'Carga marcada como falhada.')
    
    return redirect('loads:detail', pk=pk)
