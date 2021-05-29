from random import randrange
from django.shortcuts import render, redirect
from .models import Subject, Vote
from .forms import SubjectForm, VoteForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:detail', form.instance.pk)
    else:
        form = SubjectForm()
    context = {
        'form': form,
    }
    return render(request, 'votes/create.html', context)


def index(request):
    subjects = Subject.objects.order_by('-pk')
    context = {
        'subjects': subjects,
    }
    return render(request, 'votes/index.html', context)


def detail(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    votes = subject.vote_set.all()
    if votes:
        t_percent = int((votes.filter(choice=True).count() / votes.count()) * 100)
        f_percent = 100 - t_percent
    else:
        t_percent, f_percent = 50, 50
    form = VoteForm()
    context = {
        'subject': subject,
        'votes': votes,
        't_percent': t_percent,
        'f_percent': f_percent,
        'form': form,
    }
    return render(request, 'votes/detail.html', context)


def vote(request, subject_pk):
    form = VoteForm(request.POST)
    vote = form.save(commit=False)
    vote.subject = Subject.objects.get(pk=subject_pk)
    vote.save()
    return redirect('votes:detail', subject_pk)


def random(request):
    pk = randrange(1, Subject.objects.all().count()+1)
    return redirect('votes:detail', pk)