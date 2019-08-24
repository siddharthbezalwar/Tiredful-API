# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from broken_token.models import SecurityQuestion, blacklist
from broken_token.serializers import SecurityQuestionSerializer
from broken_token.lib.JwtTokenManger import JwtToken
from broken_token.decorators import authenticate_jwt_none, authenticate_jwt_hs256, jwt_user_logged_in

from time import time



# Index for JWT token scenarios
def index(request):
    """
    For JWT token generation and scenarios
    """
    return render(request, 'broken_token/index.html', )



# Index page for JWT Token - Information Disclosure
def info_disclosure(request):
	"""
	For JWT Token- Information Disclosure
	"""
	return render(request, 'broken_token/info-disclosure.html', )

# Index page for JWT Token - None algorithm
def jwt_none(request):
	"""
	For JWT Token - None algorithm challenge
	"""
	return render(request, 'broken_token/jwt-none.html', )	

# Index page for JWT Token - Signing algorithm override
def jwt_signing_algo(request):
	"""
	For JWT Token- Signing algorithm override
	"""
	return render(request, 'broken_token/jwt-signing-algo.html', )

# Index page for JWT Token - Insecure Logout
def jwt_logout(request):
	"""
	For JWT Token - Insecure Logout Scenario
 	""" 
 	return render(request, 'broken_token/jwt-insecure-logout.html', )

# Index page for JWT Token - Token Brute Force
def crack_jwt(request):
	"""
	For JWT Token- Token Brute Force
	"""
	return render(request, 'broken_token/crack-token.html', )


# JWT information disclosure scenario - HS256 signed token
@api_view(['POST'])
def get_jwt_token_HS256(request):
	''' View to get HS256 signed token '''
	if request.method == 'POST':
		if request.data:
			if 'username' in request.data.keys() and 'password' in request.data.keys():
				username = request.data['username']
				password = request.data['password']
				# signing_alg = request.data['alg']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					try:
						security_question = SecurityQuestion.objects.get(user = user)
						serializers = SecurityQuestionSerializer(security_question)
						user_group = user.groups.values_list('name',flat=True)[0]
						token_payload = dict()
						token_payload = {
							'user': user.username, 
							'email': user.email, 
							'security_question': serializers.data['question'], 
							'security_answer': serializers.data['answer'],
							'group': user_group,
							'exp': int(time()) + 3600
							}
						token = JwtToken(payload = token_payload)
						jwt_token = token.token_HS256()
						return JsonResponse({'token': jwt_token}, safe=False)

					except SecurityQuestion.DoesNotExist:
						return Response(status=status.HTTP_404_NOT_FOUND)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)


# JWT information disclosure scenario - RS256 signed token
@api_view(['POST'])
def get_jwt_token_RS256(request):
	''' View to get RS256 signed token '''
	if request.method == 'POST':
		if request.data:
			if 'username' in request.data.keys() and 'password' in request.data.keys():
				username = request.data['username']
				password = request.data['password']
				# signing_alg = request.data['alg']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					try:
						security_question = SecurityQuestion.objects.get(user = user)
						serializers = SecurityQuestionSerializer(security_question)
						user_group = user.groups.values_list('name',flat=True)[0]
						token_payload = dict()
						token_payload = {
							'user': user.username, 
							'email': user.email, 
							'security_question': serializers.data['question'], 
							'security_answer': serializers.data['answer'],
							'group': user_group,
							'exp': int(time()) + 3600
						}
						token = JwtToken(payload = token_payload)
						jwt_token = token.token_RS256()
						return JsonResponse({'token': jwt_token}, safe=False)

					except SecurityQuestion.DoesNotExist:
						return Response(status=status.HTTP_404_NOT_FOUND)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)



# JWT token for token validation scenarios - HS256 signed token
@api_view(['POST'])
def obtain_jwt_token_HS256(request):
	''' View to get HS256 signed token for token validation scenarios'''
	if request.method == 'POST':
		if request.data:
			if 'username' in request.data.keys() and 'password' in request.data.keys():
				username = request.data['username']
				password = request.data['password']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					user_group = user.groups.values_list('name',flat=True)[0]
					token_payload = {
						'user': user.username,
						'email': user.email,
						'group': user_group,
						'exp': int(time()) + 3600
					}
					token = JwtToken(payload = token_payload)
					jwt_token = token.token_HS256()
					return JsonResponse({'token': jwt_token}, safe=False)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)



# JWT token for token validation scenarios - RS256 signed token
@api_view(['POST'])
def obtain_jwt_token_RS256(request):
	''' View to get RS256 signed token for token validation scenarios'''
	if request.method == 'POST':
		if request.data:
			if 'username' in request.data.keys() and 'password' in request.data.keys():
				username = request.data['username']
				password = request.data['password']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					user_group = user.groups.values_list('name',flat=True)[0]
					token_payload = {
						'user': user.username,
						'email': user.email,
						'group': user_group,
						'exp': int(time()) + 3600
					}
					token = JwtToken(payload = token_payload)
					jwt_token = token.token_RS256()
					return JsonResponse({'token': jwt_token}, safe=False)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authenticate_jwt_none
def joker_plan(request):
	secret_target = {'plan': 'Going to rob all the mafia controlled banks of gotham'}
	return JsonResponse(secret_target, safe=False)

@api_view(['GET'])
@authenticate_jwt_hs256
def joker_master_plan(request):
	secret_target = {'plan': 'Kill all Public figures of Gotham till Batman reveals his identity'}
	return JsonResponse(secret_target, safe=False)



@api_view(['GET'])
@jwt_user_logged_in
def broken_logout(request):
	data = {'url': reverse('broken-token:index',request=request) ,'msg': 'User logged out successfully'}
	return Response(status=status.HTTP_302_FOUND, data=data)


@api_view(['GET'])
@jwt_user_logged_in
def secure_logout(request):
	try:
		JWT_tokens = blacklist.objects.get(token=request.META['HTTP_AUTHORIZATION'])
		data = {'url': reverse('broken-token:index',request=request), 'msg': 'Invalid token'}
	except blacklist.DoesNotExist:
		destroy_token = blacklist(token=request.META['HTTP_AUTHORIZATION'])
		destroy_token.save()
		data = {'url': reverse('broken-token:index',request=request), 'msg': 'User logged out successfully'}
	return Response(status=status.HTTP_302_FOUND, data=data)
