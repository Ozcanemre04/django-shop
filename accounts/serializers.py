
# serializers.py in the users Django app
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

from accounts.models import account


class CustomRegisterSerializer(RegisterSerializer):
  username = serializers.RegexField(min_length=1, regex=r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$",required=True)
  first_name = serializers.RegexField(min_length=1, regex=r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$",required=True)
  last_name = serializers.RegexField(min_length=1, regex=r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$",required=True)

  @transaction.atomic
  def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user
    

class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    class Meta(UserDetailsSerializer.Meta):
        model = account
        fields =('pk','username','email','first_name','last_name','is_superuser',)
        read_only_fields=('pk','email','is_superuser',)
