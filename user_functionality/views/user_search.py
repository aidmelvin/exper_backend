from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from exper_backend import settings


# this is for users searching for each other
class UserSearch(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return Response({"Error": "Not Logged In"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return Response({"Error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        state = request.data['state']
        school = request.data['school']
        interests = request.data['interests']
        year = request.data['year']
        major = request.data['major']
        name = request.data['name']

        return Response({}, status.HTTP_200_OK)
