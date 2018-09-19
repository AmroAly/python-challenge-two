
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('create/', views.create_email, name='create_email'),
    path('list/', views.emails_list, name='emails_list')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
