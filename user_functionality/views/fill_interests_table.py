
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_functionality.models.interest import Interest


class FillInterestsTable(APIView):
    def post(self, request):
        interestsList = [
            "Music",
            "Gym",
            "Excercise",
            "Running",
            "Cycling",
            "Biking",
            "Swimming",
            "Reading",
            "Video games",
            "Cooking",
            "TV",
            "Climbing",
            "Pets",
            "Dogs",
            "Cats",
            "Painting",
            "Jogging",
            "Skeet shooting"
        ]

        for element in interestsList:
            interest = Interest(name=element)
            interest.save()

        return Response({"message": "success"}, status.HTTP_200_OK)
