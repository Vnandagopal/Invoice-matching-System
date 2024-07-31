from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_invoice, name='upload_invoice'),
    path('match/<int:invoice_id>/', views.match_invoice, name='match_invoice')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)