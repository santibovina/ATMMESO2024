from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from operaciones.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('operaciones/', include('operaciones.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Administrador ATMmeso"
admin.site.index_title = "ATMmeso Admin"