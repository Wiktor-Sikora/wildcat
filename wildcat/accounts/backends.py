from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class AuthenticationBackend(ModelBackend):
    '''Allows users to log with their email or login'''
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(Q(username__iexact=username)|Q(email__iexact=username))
            print(user)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            pass
    
    def get_user(self, user_id):
        # the documentation says it has to be here so I put it in :)
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None