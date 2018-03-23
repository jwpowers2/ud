# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
        # I need to get message user id not session user id and pass it in url
        # this is always getting the user that is logged in
        user = Users.objects.filter(id=message.user_message_id.id)
        m_dict['first_name'] = user[0].first_name
        m_dict['last_name'] = user[0].last_name
        
        m_dict['message'] = message.message
        m_dict['id'] = message.id
        m_dict['created_at'] = message.created_at
        m2.append(m_dict)
    
    for message in m2:
        comment_dict = {}
        
        # I am showing the logged in user as author of the message -- not the person who wrote it

        print message
        comments = Comments.objects.filter(user_message_id = message['id'])
        
        
        comment_dict['comment_list'] = list(comments)
        # how do I attach user info to comments
        message['comments'] = comment_dict
        #print message

    context = { 'm_list':m2}
    return render(request, 'users/show_user.html', context)
    #return redirect("/")
def new(request):

    if request.session['status'] == False:
        return redirect('/')

    context = {
        "word":"stuff"
    }
    return render(request, 'users/new_user.html', context)

def admin_edit_user(request):

    if request.session['status'] == False:
        return redirect('/')

    context = {
        "word":"stuff"
    }
    return render(request, 'users/edit_user.html', context)

def edit_user(request,id):

    if request.session['status'] == False:
        return redirect('/')

    context = {
        "word":"stuff"
    }
    return render(request, 'users/admin_edit_user.html', context)

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

    # I need user id and message id to get the objects to create this
    user = Users.objects.get(id=userid)
    message = Messages.objects.get(id=messageid)
    Comments.objects.create(comment=request.POST['comment'],user_message_id=message,user_comment_id=user)
    messages.info(request, "message received")
    return redirect('/users/show/{}'.format(user.id))


    '''
    errors = Comments.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
    else:
        try:
            # I need user id and message id to get the objects to create this
            user = Users.objects.get(id=userid)
            message = Messages.objects.get(id=messageid)
            Comments.objects.create(comment=request.POST['comment'],user_message_id=message,user_comment_id=user)
            messages.info(request, "message received")
            return redirect('/users/show/{}'.format(user.id))

        except:
            messages.error(request, "error with message")
            return redirect('/users/show/{}'.format(id))

        return redirect('/register')
    '''
def decision(request):

    # decide to redirect to admin or to index depending on user leve
    print request.session['id']    
    user = Users.objects.get(id=request.session['id'])
    if user.user_level == '1':
        return redirect('/users/edit_user')
    if user.user_level == '9':
        return redirect('/dashboard/admin')
    return redirect('/users/admin_edit_user')
