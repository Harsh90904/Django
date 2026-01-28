from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.home, name='members'),
    path('culture/', views.culture, name='culture'),
    path('history/', views.history, name='history'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)