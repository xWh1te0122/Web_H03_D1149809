from django.urls import path
from . import views

urlpatterns = [
    path('court/', views.court, name='court'),
    path('court/detail/<int:id>',views.details,name = 'detail')
]