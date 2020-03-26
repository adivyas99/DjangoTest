from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html', {'person_name':'Cool Man'})

def add(request):

	val1 = int(request.POST['number1'])
	val2 = int(request.POST['number2'])
	result = val1 +val2

	return render(request,"answer.html", {"res":result})


## djanngo-admin --version
# create folder on desktop --mainpage
#move to its dir
## django-admin startproject coolpro #project name
## cd coolpro
##python manage.py runserver
# if face any issue in migrating then--
##python manage.py migrate
##python manage.py startapp av    #app name
##
