from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Income
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    context = {
        'title':'Budget me',
        'posts': Income.objects.all(),
    }
    return render(request, 'forum/home.html', context)

class IncomeListView(ListView):
    model = Income
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 1

class UserIncomeListView(ListView):
    model = Income
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Income.objects.filter(user=user).order_by('-date_posted')

class IncomeDetailView(DetailView):
    model = Income
    template_name = 'forum/income_detail.html'

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = [ 
        'income', 
        'rate',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    fields = [ 
        'income', 
        'rate',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.user

class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    success_url = '/'

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.user

def about(request):
    context = {
        'title':'About',
    }
    return render(request, 'forum/about.html', context)