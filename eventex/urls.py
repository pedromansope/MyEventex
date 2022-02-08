from django.contrib import admin
from core.views import home
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('subscriptions.urls')),
    path('admin/', admin.site.urls),
]
