from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddIssueForm, AddCommentForm
from .models import Issue, Comment

# Create your views here.

def list(request):
    issues = Issue.objects.filter(resolution__isnull=True)
    return render(request, "list.html", {"issues": issues})


def view(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    comments = issue.comments.order_by("created_at")
    add_comment_form = AddCommentForm()
    return render(
        request,
        "view.html",{
            "issue": issue,
            "add_comment_form": add_comment_form,
            "comments": comments,
        }
    )


def add(request):
    if request.method == "POST":
        form = AddIssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            return redirect("view", issue_id=issue.id)
    else:
        form = AddIssueForm()
    return render(request, "add.html", {"form": form})


def comment(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.created_by = request.user
            comment.save()
            return redirect("view", issue_id=issue.id)
    else:
        form = AddCommentForm()
    return render(request, "comment.html", {"form": form})