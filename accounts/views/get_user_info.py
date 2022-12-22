from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import jwt
from exper_backend import settings
from accounts.models.regular_user import RegularUser
from user_functionality.models.user_interests import UserInterests
from user_functionality.models.interest import Interest


class GetUserInfo(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"Error": "Not Logged In"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return Response({"Error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        # the id field of the jwt token is the email
        user = User.objects.get(email=payload['id'])
        full_user: RegularUser = user.regularuser

        # finding all interests
        interests_search_results = UserInterests.objects.filter(user=full_user)
        interests = []

        for element in interests_search_results:
            interests.append(element.interest.name)

        # TODO: implement error handling for if a user does not exist, return 400 error or something

        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "university_email": user.email,
            "phone_number": full_user.phone_number,
            "university": full_user.university,
            "gender": full_user.gender,
            "preference": full_user.preference,
            "year": full_user.year,
            "short_bio": full_user.short_bio,
            "age": full_user.age,
            "interests": interests
        }, status.HTTP_200_OK)
