from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.core.context_processors import csrf
from forms import *
from models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import hashlib
import datetime
import random
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            # Get user by username
            user = User.objects.get(username=username)

            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
                                      key_expires=key_expires)
            new_profile.save()
            return redirect('/todo/login', {})

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/todo/login/')
def feedback(request):
    if(request.method == 'POST'):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/add')

    else:
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})


@login_required(login_url='/todo/login/')
def index(request):
    todo = Todo1.objects.all()[:50]
    context = {
        'todos': todo
    }
    return render(request, 'index.html', context)


@login_required(login_url='/todo/login/')
def details(request, id):
    todo = Todo1.objects.get(id=id)
    print todo
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


@login_required(login_url='/todo/login/')
def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo1(title=title, text=text)
        todo.save()
        return redirect('/todo')
    else:
        return render(request, 'add.html')


@login_required(login_url='/todo/login/')
def delete(request):
    if(request.method == 'POST'):
        id = request.POST['id']
        todo = Todo1(id=id)
        todo.delete()
        return redirect('/todo')
    else:
        todo = Todo1.objects.all()
        context = {
            'todos': todo
        }
        return render(request, 'delete.html', context)


@login_required(login_url='/todo/login/')
def update(request):
    if(request.method == 'POST'):
        id = request.POST['id']
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo1(id=id)
        todo.title = title
        todo.text = text
        todo.save()
        return redirect('/todo')
    else:
        todo = Todo1.objects.all()
        context = {
            'todos': todo
        }
        return render(request, 'update.html', context)


def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = authenticate(username=username, password=password)

        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                return render(request, 'add.html', {'username': username})
            else:
                return HttpResponse("Disabled account")

        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request, 'login.html', {})


def logout1(request):
    logout(request)
    return redirect('/todo/login')
