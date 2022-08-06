from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

from users.views import login,register,profile

app_name = 'users'

urlpatterns = [
    path('login/',login,name = 'login'),
    path('register/', register, name='register'),
    path('profile/',profile,name = 'profile'),
    path('exit/', views.LogoutView.as_view(next_page = 'index'), name = 'exit')
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)