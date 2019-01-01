from django.shortcuts import render
from .models import Contact
import requests
import json
# Create your views here.



def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'blog/index.html', context)
    else:
        firstname = 'Shoaib'
        lastname = 'Khan'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'blog/index.html', context)

def contact(request):
    if request.method=='POST':
        emailr=request.POST.get('email')
        subjectr=request.POST.get('subject')
        messager=request.POST.get('message')
        c=Contact(Email=emailr,Subject=subjectr,message=messager)
        c.save()
        return render(request,'blog/thank.html')
    else:
        return render(request,'blog/contact.html')
def portfolio(request):
    return render(request,'blog/portfolio.html')
