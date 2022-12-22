from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import jwt
from exper_backend import settings
import datetime


class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data['username']
        password = request.data['password']

        if user.strip() != "" and password.strip() != "":
            try:
                user_in_question = User.objects.get(email=user)

                if user_in_question.check_password(password):
                    payload = {
                        'id': user,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                        'iat': datetime.datetime.utcnow()
                    }

                    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                    response = Response()
                    # TODO: set secure=True and sameSite=True for this cookie
                    response.set_cookie(key='jwt', value=token, httponly=True)
                    response.status_code = status.HTTP_202_ACCEPTED
                    response.data = {
                        # 'jwt': token,
                        'message': 'success'
                    }

                    return response
                else:
                    return Response({"message": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"message": "No user with that email"}, status=status.HTTP_400_BAD_REQUEST)
            except User.MultipleObjectsReturned:
                return Response({"Error": "Multiple users with that email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"Error": "Blank username or password field"}, status=status.HTTP_400_BAD_REQUEST)
