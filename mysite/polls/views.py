from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

"""
When somebody requests a page from your website – say, “/polls/34/”, 
Django will load the mysite.urls Python module because it’s pointed to 
by the ROOT_URLCONF setting. It finds the variable named urlpatterns and 
traverses the patterns in order. After finding the match at 'polls/', it 
strips off the matching text ("polls/") and sends the remaining text – "34/" – 
to the ‘polls.urls’ URLconf for further processing. There it matches 
'<int:question_id>/', resulting in a call to the detail() view like so:
detail(request=<HttpRequest object>, question_id=34)
"""
