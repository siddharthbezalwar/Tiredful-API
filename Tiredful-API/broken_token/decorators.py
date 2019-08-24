from django.core.exceptions import PermissionDenied
from broken_token.lib.JwtTokenManger import JwtToken
from broken_token.models import blacklist

# For authenticating user with unsigned JWT token
def authenticate_jwt_none(function):
	def wrap(request, *args, **kwargs):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			if request.META['HTTP_AUTHORIZATION']:
				try:
					destroyed_token = blacklist.objects.get(token=request.META['HTTP_AUTHORIZATION'])
					raise PermissionDenied
				except blacklist.DoesNotExist:
					pass
				except:
					raise PermissionDenied

				jwt_token = JwtToken(request.META['HTTP_AUTHORIZATION'])
				status = jwt_token.decode_user_jwt_token()
				if status:
					return function(request, *args, **kwargs)
				else:
					raise PermissionDenied
			else:
				raise PermissionDenied
		else:
			raise PermissionDenied

	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap


# For authenticating user with overwritten signing algorithm
def authenticate_jwt_hs256(function):
	def wrap(request, *args, **kwargs):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			if request.META['HTTP_AUTHORIZATION']:
				try:
					destroyed_token = blacklist.objects.get(token=request.META['HTTP_AUTHORIZATION'])
					raise PermissionDenied
				except blacklist.DoesNotExist:
					pass
				except:
					raise PermissionDenied
				jwt_token = JwtToken(request.META['HTTP_AUTHORIZATION'])
				status = jwt_token.decode_user_jwt_token_hs256()
				if status:
					return function(request, *args, **kwargs)
				else:
					raise PermissionDenied
			else:
				raise PermissionDenied
		else:
			raise PermissionDenied

	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

# To check user is authenticated
def jwt_user_logged_in(function):
	def wrap(request, *args, **kwargs):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			if request.META['HTTP_AUTHORIZATION']:
				return function(request, *args, **kwargs)
			else:
				raise PermissionDenied
		else:
			raise PermissionDenied

	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap	
