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

from django.conf.urls import url
from . import views

urlpatterns = [

    # ex: /jwt-token/
    url(r'^$', views.index, name='index'),

    # ex: /jwt-token/info-disclosure
    url(r'^info-disclosure/$', views.info_disclosure, name='info-disclosure'),

    # ex: /jwt-token/jwt-none/
    url(r'^jwt-none/$', views.jwt_none, name='jwt-none'),

    # ex: /jwt-token/jwt-signing-algo/
    url(r'^jwt-signing-algo/$', views.jwt_signing_algo, name='jwt-signing-algo'),

    # ex: /jwt-token/jwt-logout/
    url(r'^jwt-logout/$', views.jwt_logout, name='jwt-logout'),

    # ex: /crack-jwt/
    url(r'^crack-jwt/$', views.crack_jwt, name='crack-jwt'),

    # ex: /get-jwt-token-hs256/
    url(r'^get-jwt-token-hs256/$', views.get_jwt_token_HS256, name='get-jwt-token-hs256'),

    # ex: /get-jwt-token-rs256/
    url(r'^get-jwt-token-rs256/$', views.get_jwt_token_RS256, name='get-jwt-token-rs256'),

    # ex: /obtain-jwt-token-hs256/
    url(r'^obtain-jwt-token-hs256/$', views.obtain_jwt_token_HS256, name='obtain-jwt-token-hs256'),

    # ex: /obtain-jwt-token-rs256/
    url(r'^obtain-jwt-token-rs256/$', views.obtain_jwt_token_RS256, name='obtain-jwt-token-rs256'),

    # ex: /joker-plan/
    url(r'^joker-plan/$', views.joker_plan, name='joker-plan'),

    # ex: /joker-master-plan/
    url(r'^joker-master-plan/$', views.joker_master_plan, name='joker-master-plan'),

    # ex: /logout/
    url(r'^logout/$', views.broken_logout, name='logout'),

    # ex: /secure-logout/
    url(r'^secure-logout/$', views.secure_logout, name='secure-logout'),



]
