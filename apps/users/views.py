# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.shortcuts import render,redirect
from django.contrib import messages
from django.apps import apps
Users = apps.get_model('login', 'Users')
Messages = apps.get_model('login', 'Messages')
Comments = apps.get_model('login', 'Comments')


def logoff(request):

    del request.session['status']
    return redirect("/")

def show(request,id):

    if request.session['status'] == False:
        return redirect('/')

    messages = Messages.objects.all()
    m1 = list(messages)
    m2 = []

    for message in m1:

        m_dict = {}
        user = Users.objects.filter(id=message.user_message_id.id)
        m_dict['first_name'] = user[0].first_name
        m_dict['last_name'] = user[0].last_name
        
        m_dict['message'] = message.message
        m_dict['id'] = message.id
        m_dict['created_at'] = message.created_at
        m2.append(m_dict)
    
    for message in m2:
        comment_dict = {}
        print message
        comments = Comments.objects.filter(user_message_id = message['id'])
        comment_dict['comment_list'] = list(comments)
        message['comments'] = comment_dict

    context = { 'm_list':m2}
    return render(request, 'users/show_user.html', context)

def new(request):

    if request.session['status'] == False:
        return redirect('/')

    messages.info(request, "")

    context = {
        "word":"stuff"
    }
    return render(request, 'users/new_user.html', context)

def show_profile(request,profile_id):

    if request.session['status'] == False:
        return redirect('/')
    messages.info(request, "")
    user = Users.objects.filter(id=profile_id)
    context = {
               'name': '{} {}'.format(user[0].first_name, user[0].last_name),
               'email': user[0].email,
               'id':user[0].id
              }
    return render(request, 'users/show_profile.html', context)

def admin_edit_user(request,id_to_edit):

    if request.session['status'] == False:
        return redirect('/')
    messages.info(request, "")
    errors = Users.objects.basic_validator(request.POST)
    user_to_edit = Users.objects.filter(id=id_to_edit)
    context = {
        "first_name":user_to_edit[0].first_name,
        "id":user_to_edit[0].id
    }
    return render(request, 'users/admin_edit_user.html', context)

def edit_user(request,id_to_edit):

    if request.session['status'] == False:
        return redirect('/')
    messages.info(request, "")
    errors = Users.objects.basic_validator(request.POST)
    user_to_edit = Users.objects.filter(id=id_to_edit)
    context = {
        "first_name":user_to_edit[0].first_name,
        "id":user_to_edit[0].id
    }
    return render(request, 'users/edit_user.html', context)

def update_user(request,id_to_update):

    if request.session['status'] == False:
        return redirect('/')
    messages.info(request, "")
    errors = Users.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        user = Users.objects.filter(id=id_to_update)
        user = user[0]

        if request.POST['first_name']:
            user.first_name = request.POST['first_name']
        if request.POST['last_name']:
            user.last_name = request.POST['last_name']
        if request.POST['email']:
            user.email = request.POST['email']
        if request.POST['password']:
            user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        user.save() 
        return redirect('/dashboard')
    
    return redirect('/users/admin_edit_user/{}'.format(id_to_update))

def remove_user(request, id):
    
    if id != request.session['id']:

        d = Users.objects.filter(id=id) 
        d.delete()
        return redirect('/dashboard/decision')

    else:

        # delete yourself and go back home
        d = Users.objects.filter(id=id) 
        d.delete()

        return redirect('/')

def create_message(request, id):

    errors = Messages.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
    else:
        try:
            user = Users.objects.get(id=id)
        
            Messages.objects.create(message=request.POST['message'],user_message_id=user)
            messages.info(request, "message received")
            return redirect('/users/show/{}'.format(user.id))

        except:
            messages.error(request, "error with message")
            return redirect('/users/show/{}'.format(id))

        return redirect('/register')
        
def create_comment(request, messageid, userid):

    try:
        user = Users.objects.get(id=userid)
        message = Messages.objects.get(id=messageid)
        Comments.objects.create(comment=request.POST['comment'],user_message_id=message,user_comment_id=user)
        
        return redirect('/users/show/{}'.format(user.id))
    except:
        return redirect('/users/show/{}'.format(user.id))

def decision(request,id_to_edit):

    user = Users.objects.get(id=request.session['id'])
    if user.user_level == '1':
        return redirect('/users/edit_user/{}/'.format(id_to_edit))
    if user.user_level == '9':
        return redirect('/users/admin_edit_user/{}/'.format(id_to_edit))
    return redirect('/users/admin_edit_user/{}/'.format(id_to_edit))
