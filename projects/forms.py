from django.forms import ModelForm
from  django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image',
                  'project']
        labels = {
            'title':'عنوان پروژه',
            'featured_image':'عکسی برای پروژه انتخاب کنید',
            'project': 'پروژه خود را آپلود کنید',
        }

    def __init__(self , *args , **kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'add title'})
        self.fields['project'].widget.attrs.update({'class': 'input'})
        self.fields['featured_image'].widget.attrs.update({'class': 'input'})