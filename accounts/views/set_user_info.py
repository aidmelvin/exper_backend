from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import jwt
from exper_backend import settings
from accounts.models.regular_user import RegularUser
from user_functionality.models.user_interests import UserInterests
from user_functionality.models.interest import Interest


class SetUserInfo(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            print('there is no token')
            return Response({"Error": "Not Logged In"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            print('token decoding failed')
            return Response({"Error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        # the id field of the jwt token is the email
        user = User.objects.get(email=payload['id'])
        full_user: RegularUser = user.regularuser
        response = Response()
        response.data = {
            'message': 'success'
        }

        # TODO: implement error handling for if a user does not exist, return 400 error or something

        new_first_name = request.data["first_name"]
        new_last_name = request.data["last_name"]

        new_university_email = request.data["university_email"]
        new_phone_number = request.data["phone_number"]

        new_university = request.data["university"]

        new_gender = request.data["gender"]
        new_preference = request.data["preference"]
        new_year = request.data["year"]
        new_age = request.data["age"]
        new_short_bio = request.data["short_bio"]

        new_interests = request.data['interests']

        user.first_name = new_first_name
        user.last_name = new_last_name

        if user.username != new_university_email:
            response.delete_cookie('jwt')

        user.username = new_university_email
        user.email = new_university_email

        full_user.phone_number = new_phone_number
        full_user.university = new_university
        full_user.gender = new_gender
        full_user.preference = new_preference
        full_user.year = new_year
        full_user.age = new_age
        full_user.short_bio = new_short_bio

        for element in UserInterests.objects.filter(user=full_user):
            element.delete()

        for new_interest_name in new_interests:
            new_interest = UserInterests(user=full_user, interest=Interest.objects.get(name=new_interest_name))
            new_interest.save()

        user.save()
        full_user.save()

        return response
