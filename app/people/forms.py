from django import forms
from app.people import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Submit


class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.include_media = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 '),
                Column('middle_name', css_class='form-group col-md-4 '),
                Column('last_name', css_class='form-group col-md-4 '),
            ),
            Row(
                Column('relationship', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('is_in_personal_life', css_class='form-group col-md-12 mb-0'),
                Column('is_in_work_life', css_class='form-group col-md-12 mb-0'),
            ),
        )
        self.helper.add_input(Submit('Submit', 'Submit'))

    class Meta:
        model = models.People
        exclude = [
        ]
        labels = {
        }
        widgets = {
        }