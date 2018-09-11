from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')