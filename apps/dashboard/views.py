# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render,redirect
from django.apps import apps
Users = apps.get_model('login', 'Users')
Messages = apps.get_model('login', 'Messages')
Comments = apps.get_model('login', 'Comments')


USER_LEVEL = {'1': 'user', '9': 'admin'}

def logoff(request):

    del request.session['status']
    return redirect("/")

def index(request):
    messages.info(request, "")

    if request.session['status'] == False:
        return redirect('/')

    users = Users.objects.all()
    users1 = list(users)
    
    users2 = [{'id':x.id,
               'first_name':x.first_name, 
               'last_name':x.last_name, 
               'email':x.email, 
               'created_at':x.created_at, 
               'user_level':USER_LEVEL[x.user_level]} for x in users1]

    context = { 'user_list':users2}
    return render(request, 'dashboard/index.html',context)

def admin(request):

    messages.info(request, "")
    if request.session['status'] == False:
        return redirect('/')

    users = Users.objects.all()
    users1 = list(users)
    users2 = [{'id':x.id,
               'first_name':x.first_name, 
               'last_name':x.last_name, 
               'email':x.email, 
               'created_at':x.created_at, 
               'user_level':USER_LEVEL[x.user_level]} for x in users1]

    context = { 'user_list':users2}
    return render(request, 'dashboard/admin.html',context)

def decision(request):

    user = Users.objects.get(id=request.session['id'])
    if user.user_level == '1':
        return redirect('/dashboard/')
    if user.user_level == '9':
        return redirect('/dashboard/admin')
    return redirect('/dashboard/admin')
