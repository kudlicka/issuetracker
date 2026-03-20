from django import forms
from .models import Issue, Comment, Screenshot

class AddIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description_md', 'issue_type', 'due_date']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "description_md"]


class AddScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ["screenshot"]