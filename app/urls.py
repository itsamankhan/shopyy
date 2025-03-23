from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm)),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('details/<int:id>/', views.ProductDetailView.as_view(), name="details"),
    path('profile/', views.profile, name="profile"),
    path('cart/', views.cart, name="cart"),
    path('add-to-cart/', views.add_to_cart, name="addCart"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# a62