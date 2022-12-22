from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from accounts.models.regular_user import RegularUser
from rest_framework import status
from user_functionality.models.user_interests import UserInterests
from user_functionality.models.interest import Interest


class CreateAccountView(APIView):
    def post(self, request, format=None):
        # if account creation is successful then we redirect
        # to login page

        first_name = request.data['first_name']
        last_name = request.data['last_name']
        university = request.data['university']
        university_email = request.data['university_email']
        year = request.data['year']
        gender = request.data['gender']
        short_bio = request.data['short_bio']
        phone_number = request.data['phone_number']
        password = request.data['password']

        age = request.data['age']
        preference = request.data['preference']

        interests = request.data['interests']

        queryset = User.objects.filter(email=university_email)
        if queryset.exists():
            return Response({"Error": "A user with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            new_user = User(username=university_email, email=university_email, first_name=first_name,
                            last_name=last_name)
            new_user.set_password(password)
            supplimental_information = RegularUser(user=new_user, university=university, year=year, gender=gender,
                                                   short_bio=short_bio, phone_number=phone_number,
                                                   age=int(age), preference=preference)

            new_user.save()
            supplimental_information.save()

            for user_interest in interests:
                existing_interest = Interest.objects.get(name=user_interest)
                new_joint_table_entry = UserInterests(user=supplimental_information, interest=existing_interest)
                new_joint_table_entry.save()

            return Response({'Success': 'account successfully created'}, status=status.HTTP_201_CREATED)
