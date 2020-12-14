from django.shortcuts import render
from django.views import generic


class WelcomeView(generic.TemplateView):
    template_name = 'welcome/welcome_page.html'

