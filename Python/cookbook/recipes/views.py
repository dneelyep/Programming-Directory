# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import recipes

def welcome(request):

    return render_to_response('welcome.html', {'MEDIA_URL': recipes.MEDIA_URL}



