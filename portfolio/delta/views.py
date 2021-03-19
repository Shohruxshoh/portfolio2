from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Contact, db_projects, Skills, Adress, Comments
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.

def index(request):
    comments = Comments.objects.all().order_by('-date')[:4]
    skills = Skills.objects.only('html', 'css', 'python')
    context = {'skills': skills, 'comment': comments}
    return render(request, 'delta/index.html', context)


def projects(request):
    project = db_projects.objects.all()
    context = {'project': project}
    return render(request, 'delta/projects.html', context)


def contact(request):
    adress = Adress.objects.all()
    context = {'adress': adress}

    if request.method == 'POST':
        contact = Contact()
        telefon = request.POST.get('telefon')
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        comment = request.POST.get('comment')
        contact.telefon = telefon
        contact.name = name
        contact.Email = Email
        contact.comment = comment
        contact.save()
        return redirect('home')

    return render(request, 'delta/contact.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'delta/register.html', context)


def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user)
            return redirect('home')
        else:
            messages.info(request, 'password is incorrect ')
    context = {}
    return render(request, 'registration/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def post_detail(request, slug):
    post = db_projects.objects.get(slug__iexact=slug)
    if request.method == 'POST':
        comments = Comments()
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        comments.name = username
        comments.description = comment
        comments.save()

    return render(request, 'delta/post_detail.html', {'post': post})
