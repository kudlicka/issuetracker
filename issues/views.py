from django.shortcuts import render, redirect
from .forms import AddIssueForm

# Create your views here.

def list(request):
    pass


def view(request, issue_id):
    pass


def add(request):
    if request.method == "POST":
        form = AddIssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            return redirect("/")
    else:
        form = AddIssueForm()
    return render(request, "add.html", {"form": form})
