from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import cv2






# Create your views here.

def ver_index(request):
    #imagen = cv2.imread('static/django.jpg')


    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    return render(request, 'index.html')