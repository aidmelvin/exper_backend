from django.http import HttpResponse, HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import RegularUser
from django.contrib.auth.models import User


class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data['username']
        password = request.data['password']

        if user.strip() != "" and password.strip() != "":
            try:
                user_in_question = User.objects.get(email=user)

                if user_in_question.check_password(password):
                    return Response({"Success": "Correct username and password"}, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({"Error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"Error": "No user with that email"}, status=status.HTTP_400_BAD_REQUEST)
            except User.MultipleObjectsReturned:
                return Response({"Error": "Multiple users with that email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"Error": "Blank username or password field"}, status=status.HTTP_400_BAD_REQUEST)


class CreateAccountView(APIView):
    def post(self, request, format=None):
        # if account creation is successful then we redirect
        # to login page
        print('sign up request received')

        first_name = request.data['first_name']
        last_name = request.data['last_name']
        university = request.data['university']
        university_email = request.data['university_email']
        year = request.data['year']
        gender = request.data['gender']
        short_bio = request.data['short_bio']
        phone_number = request.data['phone_number']
        password = request.data['password']

        queryset = User.objects.filter(email=university_email)
        if queryset.exists():
            return Response({"Error": "A user with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            new_user = User(username=university_email, email=university_email, first_name=first_name,
                            last_name=last_name)
            new_user.set_password(password)
            supplimental_information = RegularUser(user=new_user, university=university, year=year, gender=gender,
                                                   short_bio=short_bio, phone_number=phone_number)

            new_user.save()
            supplimental_information.save()
            return Response({'Success': 'account successfully created'}, status=status.HTTP_201_CREATED)
