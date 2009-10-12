from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
	return render_to_response('login.html')

def logout(request):
    return HttpResponse(request.user)