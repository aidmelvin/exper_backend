from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import jwt
from exper_backend import settings


class HomePageView(APIView):
    def get(self, request):
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

        # TODO: implement error handling for if a user does not exist, return 400 error or something

        return Response({"name": user.first_name}, status.HTTP_200_OK)
