
from django.urls import include, path, re_path

from django.conf import settings
from django.conf.urls.static import static


# from core.views.admin import view_admin, view_organization, view_role
from core.views import view_auth, view_home

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', view_home.HomeView.as_view(), name='home'),
    path('login', view_auth.LoginView.as_view(), name='login'),
    path('logout', login_required(view_auth.LogoutView.as_view()) , name ='logout')
]