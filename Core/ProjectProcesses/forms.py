
from django.forms import ModelForm, TextInput, Select, FileInput, Textarea

from Core.ProjectProcesses.models import Project


class ProjectCreateForm (ModelForm):
    field_order = ('name','area','evaluation','start_date','image')

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('state','end_date')
        widgets = {
            'area': Select(
                attrs = {
                    'class':'form-control select2 select2-hidden-accessible',
                    'style' : 'width: 100%;'
                }
            ),
            'start_date': TextInput(
                attrs= {
                    'class': 'datetimepicker-input',
                    'data-target': '#reservationdate',
                },
            ),
            'fundamentation': Textarea(
                attrs={
                    'rows': 3
                }
            ),
            'conclution': Textarea(
                attrs={
                    'rows': 3
                }
            ),
            'recomendation': Textarea(
                attrs={
                    'rows': 3
                }
            ),

        }