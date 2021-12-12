from django.forms import ModelForm
from django import forms


from client.models import Expertise
from projectapp.models import Project


class ExpertiseCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Expertise
        fields = ['project', 'title', 'image', 'content']



