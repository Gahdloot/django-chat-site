from django.shortcuts import render
from .models import Draft, Message
from django.http import HttpResponse


# Create your views here.

def index(request):
    Messages = Message.objects.all()
    Drafts = Draft.objects.all()
    context = {'messages': Messages, 'drafts': Drafts}
    return render(request, 'messageApp/Index.html', context)