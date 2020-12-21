from django.shortcuts import render, reverse,get_object_or_404
from django.views import generic
from app.people import models, forms


class PeopleListView(generic.ListView):
    template_name = 'people/people_list_page.html'
    queryset = models.People.objects.all()
    context_object_name = 'people_list'


class PeopleFormView(generic.UpdateView):
    template_name = 'core/page/page_form.html'
    form_class = forms.PeopleForm
    model = models.People

    def get_object(self, *args, **kwargs):
        if self.kwargs['pk'] != 0:
            return get_object_or_404(models.People, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form_title'] = 'Create New Person'
        if self.kwargs['pk'] != 0:
            context_data['form_title'] = 'Edit ' + str(self.object.first_name)
        return context_data

    def get_success_url(self):
        return reverse('people_list')

