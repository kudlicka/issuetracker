from django import forms
from .models import Issue

class AddIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description_md', 'issue_type', 'due_date']
