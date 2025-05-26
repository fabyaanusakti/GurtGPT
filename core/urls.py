from django.urls import path
from . import views

urlpatterns = [
    path('GurtGPT/', views.chat_view, name='ask_gurt'),
]