from django.urls import path
from . import views
from .views import (
    IncomeListView, 
    IncomeDetailView,
    IncomeCreateView,
    IncomeUpdateView,
    IncomeDeleteView,
    UserIncomeListView,
    AboutTemplateView,
)

urlpatterns = [
    path('', IncomeListView.as_view(), name='forum-home'),
    path('user/<str:username>', UserIncomeListView.as_view(), name='user-income'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('income/new/', IncomeCreateView.as_view(), name='income-create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
    path('about/', AboutTemplateView.as_view(), name='forum-about'),
]