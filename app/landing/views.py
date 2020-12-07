from django.shortcuts import render
from django.views import generic


class HomeDetailView(generic.TemplateView):
    template_name = 'landing/home/home_detail_view_page.html'