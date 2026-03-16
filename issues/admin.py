from django.contrib import admin

# Register your models here.
from .models import Issue, Comment, IssueType, Resolution

admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(IssueType)
admin.site.register(Resolution)



