# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Broken_token security question model
class SecurityQuestion(models.Model):
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=40)
	user = models.ForeignKey(User)

# Broken_token blacklisted tokens
class blacklist(models.Model):
	token = models.CharField(max_length=2048)
