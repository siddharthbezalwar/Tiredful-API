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

import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))


# Class to manage JWT tokens
class JwtToken:
	def __init__(self, payload):
		self.payload = payload
		self.secret = 'Just!c3'

	# Getting JWT token using HS256 signing algorithm
	def token_HS256(self):
		''' Class method to get JWT token using HS256 signing algorithm '''
		return jwt.encode(self.payload, self.secret, algorithm='HS256')

	# Method to get private key to sign token using RS256
	def __get_pvt_key__(self):
		'''Class method to get private key for singning token using RS256 algorithm'''
		fp = open("broken_token/lib/tiredful.pem","r")
		key = fp.read()
		return key


	# Method to get public key to verify token signed using RS256 signing algorithm
	def __get_pub_key__(self):
		'''Class method to get public key to verify token signed using RS256 signing algorithm'''
		fp = open("broken_token/lib/tiredful_public","r")
		key = fp.read()
		return key 

	# Method to get fake public key to demonstrate the RS256 to HS256 signing algo issue
	def __get_fake_pub_key__(self):
		'''Class method to get fake public key to demonstrate the RS256 to HS256 signing algo issue'''
		fp = open("broken_token/lib/fake_public","r")
		key = fp.read().strip()
		return key 

	# Getting JWT token using HS256 signing algorithm
	def token_RS256(self):
		''' Class method to get JWT token using HS256 signing algorithm '''
		pvt_key = self.__get_pvt_key__()
		return jwt.encode(self.payload, pvt_key, algorithm='RS256')

	# Method to decode JWT token without verifying signature i.e. with none algorithm
	def decode_user_jwt_token(self):
		user_info = ''
		try:
			user_info = jwt.decode(self.payload, verify=False)
			print user_info
		except:
			return False

		if user_info['group'] == 'Supervillains':
			return True
		else:
			False

	# Method to decode JWT token with overwritten signing algoritm (i.e. replacing RS256 by HS@56 with public key)
	def decode_user_jwt_token_hs256(self):
		user_info  = ''
		signing_algo = ''

		try:
			signing_algo = jwt.get_unverified_header(self.payload)['alg']
		except:
			return False

		try:
			if signing_algo.upper() == 'RS256':
				user_info = jwt.decode(self.payload, self.__get_pub_key__(), algorithm='RS256')
			elif signing_algo.upper() == 'HS256':
				user_info = jwt.decode(self.payload, self.__get_fake_pub_key__(), algorithm='HS256')
			else:
				return False
		except:
		 	return False

		if user_info['group'] == 'Supervillains':
			return True
		else:
			False





		
