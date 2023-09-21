import django.contrib.auth.views import LoginView
import django.urls import path

from .froms import LoginForms

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html',
                                     form_calss=LoginForms, name='login'))
]