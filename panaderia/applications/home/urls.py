from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.PanelView.as_view(),
        name='home',
    ),
    path(
        'perfil/',
        views.PanelView2.as_view(),
        name='perfil',
    ),

    # path(
    #     'users/register/',
    #     views.UserRegisterView.as_view(),
    #     name='user-register',
    # ),

]