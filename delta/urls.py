from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('projects/', views.projects, name="projects"),
    path('contacts/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail_url')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
