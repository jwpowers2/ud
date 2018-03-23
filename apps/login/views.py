# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
import bcrypt
from django.shortcuts import render,redirect
from .models import *

    
def logoff(request):

    request.session['status'] = False
    return redirect("/")

def index(request):

    if not 'status' in request.session:
        request.session['status'] = False
    if not 'first_name' in request.session:
        request.session['first_name'] = ''
    if not 'id' in request.session:
        request.session['id'] = 0

    return render(request, 'login/index.html')

def signin(request):
    
    return render(request, 'login/signin.html')

def register(request):

    return render(request, 'login/register.html')

def enter(request):

    try:

        user = Users.objects.get(email=request.POST['email'])

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):

            request.session['status'] = True
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['user_level'] = user.user_level
            return redirect('/users/show/{}'.format(user.id))

    except:
        return redirect('/signin')        


def create(request):

    errors = Users.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:

        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=password_hash, user_level=1)
        request.session['status'] = True
        user = Users.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['user_level'] = user.user_level
        return redirect('/users/show/{}'.format(user.id))

    return redirect('/register')

