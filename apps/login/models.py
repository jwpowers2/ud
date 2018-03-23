# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

class UsersManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}
        try:
            if not re.search("[a-zA-Z]{2,30}",postData['first_name']):
                errors['first_name'] = "first name must be at least two characters and only letters"
        except:
            pass
        try:
            if not re.search("[a-zA-Z]{2,30}",postData['last_name']):
                errors['last_name'] = "first name must be at least two characters and only letters"
        except:
            pass
        try:
            if not re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",postData['email']):
                errors['email'] = "not a valid email"
        except:
            pass
        try:
            if len(postData['password']) < 9:
                errors['password'] = "password is required and must be at least 8 characters"
        except:
            pass
        try:
            if not postData['password'] == postData['confirm_password']:
                errors['password'] = "password is not same as confirm password" 
        except:
            pass
        return errors


class Users(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user_level = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    objects = UsersManager()

class MessagesManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}
        try:
            if not re.search("[a-zA-Z]{2,1000}",postData['message']):
                errors['first_name'] = "message must be at least two characters and only letters"
        except:
            pass
        return errors

class Messages(models.Model):


    message = models.TextField(max_length=1000)
    user_message_id = models.ForeignKey(Users, related_name="messages") 
    created_at = models.DateTimeField(auto_now_add=True)
    objects = MessagesManager()

class CommentsManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}
        try:
            if not re.search("[a-zA-Z]{2,1000}",postData['comment']):
                errors['first_name'] = "comment must be at least two characters and only letters"
        except:
            pass
        return errors

class Comments(models.Model):

    comment = models.TextField(max_length=1000)
    user_comment_id = models.ForeignKey(Users, related_name="comments") 
    user_message_id = models.ForeignKey(Messages, related_name="comments") 
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentsManager()
