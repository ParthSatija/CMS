from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from forms import SubscriberForm
from forms import CrisisCreateForm
from forms import ReportReceiverForm
from django.core.context_processors import csrf
import datetime
# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def subscribe(request):
    return render(request, 'Subscribe.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('Login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    else:
        form = UserCreationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')

def createSubscriber(request):
    if request.POST:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/subscriber_successful')
    else:
        form = SubscriberForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('Subscribe.html', args)

def addReportReceiver(request):
     if request.POST:
        form = ReportReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/reportreceiveradded')
     else:
        form = ReportReceiverForm()
     args = {}
     args.update(csrf(request))

     args['form'] = form
     return render_to_response('add_report_receiver.html', args)

def report_reciever_added(request):
    return render_to_response('loggedin.html')

def subscriber_successful(request):
    return render_to_response('homepage.html')

def create_crisis(request):
    if request.POST:
        form=CrisisCreateForm(request.POST)
        if form.is_valid():
            crisis = form.save(commit=False);
            crisis.date = datetime.date.today()
            crisis.time = datetime.datetime.now().time()
            crisis.save()
            return HttpResponseRedirect('/crisis/status')
    else:
        form=CrisisCreateForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('create_crisis.html', args)

def status_crisis(request):
    return render_to_response('status_crisis.html')
