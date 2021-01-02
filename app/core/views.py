from django.shortcuts import render
from django.views import generic


class SearchView(generic.TemplateView):
    template_name = 'core/search/search_list_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data
