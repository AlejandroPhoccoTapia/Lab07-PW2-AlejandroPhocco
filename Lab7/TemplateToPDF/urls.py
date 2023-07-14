from django.urls import path
from . import views

urlpatterns = [
  path('pdf/', views.GeneratePDF.as_view(), name='PDF'),
]
