from rest_framework import serializers
from accounts.models.regular_user import RegularUser


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        fields = ('first_name', 'last_name', 'university', 'university_email', 'year',
                  'gender', 'short_bio', 'phone_number', 'password')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        fields = ('university_email', 'password')
