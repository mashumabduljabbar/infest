from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('author','title','text','link','priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
