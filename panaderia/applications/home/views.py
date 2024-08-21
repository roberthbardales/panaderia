from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)

class PanelView(TemplateView):
    template_name = 'panel.html'

# class PanelView2(TemplateView):
#     template_name = 'users/perfil.html'









