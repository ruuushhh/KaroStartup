from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .utils import GoogleLogin



class GoogleCalendarInitView(APIView):
 
    def get(self, request):
        credentials = GoogleLogin()
        service = build("calendar", "v3", credentials= credentials)
        result=service.calendarList().list().execute()
        return Response(result)


class GoogleCalendarRedirectView(APIView):

    def get(self, request):
        credentials = GoogleLogin()
        return Response({"Status": "Success", "message": "You have Successfully Logged in!"})



        