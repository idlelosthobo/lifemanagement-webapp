from django.shortcuts import render, reverse,get_object_or_404
from django.views import generic
from app.note import models, forms


class NoteDetailView(generic.DetailView):
    template_name = 'note/note_detail_page.html'
    model = models.Note
    context_object_name = 'note'


class NoteListView(generic.ListView):
    template_name = 'note/note_list_page.html'
    queryset = models.Note.objects.all()
    context_object_name = 'note_list'


class NoteFormView(generic.UpdateView):
    template_name = 'core/page/page_form.html'
    form_class = forms.NoteForm
    model = models.Note

    def get_object(self, *args, **kwargs):
        if self.kwargs['pk'] != 0:
            return get_object_or_404(models.Note, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form_title'] = 'Create Note'
        if self.kwargs['pk'] != 0:
            context_data['form_title'] = 'Edit ' + str(self.object.title)
        return context_data

    def get_success_url(self):
        return reverse('note_list')

