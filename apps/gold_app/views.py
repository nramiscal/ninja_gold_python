from django.shortcuts import render, HttpResponse, redirect
import random
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0
    return render(request, 'gold_app/index.html')


def process_money(request):
    print request.POST
    time = datetime.now().replace(microsecond=0)
    print time
    if request.POST['location'] == "farm":
        a = 10
        b = 20
        c = 0
    elif request.POST['location'] == "cave":
        a = 5
        b = 10
        c = 0
    elif request.POST['location'] == "house":
        a = 2
        b = 5
        c = 0
    elif request.POST['location'] == "casino":
        a = 0
        b = 50
        c = random.randint(0,1)

    gold = random.randint(a,b)
    print request.session['total_gold']
    print gold
    # print request.session['total_gold']
    if c == 0:
        request.session['total_gold'] += gold
        activity = "Earned {} golds from the {}! {}".format(gold, request.POST['location'], time)
    elif c == 1:
        request.session['total_gold'] -= gold
        activity = "Ouch... Lost {} golds from the {}... {}".format(gold, request.POST['location'], time)
    print request.session['total_gold']
    request.session['activity'] = activity

    if not 'activities' in request.session:
        list = [activity]
        # list.append(activity)
        request.session['activities'] = list
    else:
        list = request.session['activities']
        list.append(activity)
        request.session['activities'] = list

    print activity
    print request.session['activities']


    return redirect('/')
