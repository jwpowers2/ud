# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
import re
from django.db import models
from ud.login.models import Users

class UsersManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}
        
        if not re.search("[a-zA-Z]{2,30}",postData['first_name']):
            errors['first_name'] = "first name must be at least two characters and only letters"
        if not re.search("[a-zA-Z]{2,30}",postData['last_name']):
            errors['last_name'] = "first name must be at least two characters and only letters"
        if not re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",postData['email']):
            errors['email'] = "not a valid email"
        if len(postData['password']) < 9:
            errors['password'] = "password is required and must be at least 8 characters"
        if not postData['password'] == postData['confirm_password']:
            errors['password'] = "password is not same as confirm password" 
        return errors


class Users(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user_level = models.CharField(max_length=255)
    objects = UsersManager()
'''
