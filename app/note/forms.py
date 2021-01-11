from django import forms
from app.note import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Submit


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.include_media = False
        self.helper.attrs = {'data-swup-form': '', 'data-swup-transition': 'transition-fade', 'action': '?'}
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('information', css_class='form-group col-md-12 mb-0'),
            ),
        )
        self.helper.add_input(Submit('Submit', 'Submit'))

    class Meta:
        model = models.Note
        exclude = [
        ]
        labels = {
        }
        widgets = {
        }