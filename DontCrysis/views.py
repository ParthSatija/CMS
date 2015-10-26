from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from forms import SubscriberForm,CrisisCreateForm, ReportReceiverForm, CrisisForm
from django.core.context_processors import csrf
from models import Crisis, Agency, ReportReceiver
from django.core.urlresolvers import reverse_lazy
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
    crises = Crisis.objects.all().order_by('-date','-time')
    reports= ReportReceiver.objects.all()
    return render(request,'loggedin.html',{'crises' :crises, 'reports':reports})

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

#@login_required(redirect ka url)
def addReportReceiver(request):
     if request.POST:
        form = ReportReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/loggedin')
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

def crisis_create(request):
    if request.POST:
        form=CrisisCreateForm(request.POST)
        if form.is_valid():
            crisis_type=form.cleaned_data['type']
            crisis = form.save(commit=False);
            crisis.date = datetime.date.today()
            crisis.time = datetime.datetime.now().time()
            crisis.save()
            request.session['type']=crisis_type
            return HttpResponseRedirect('/crisis/status', crisis.type)
    else:
        form=CrisisCreateForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('crisis_create.html', args)

def status_crisis(request):
    crisis_type=request.session.get('type')
    agency = Agency.objects.filter(type=crisis_type)
    return render(request, 'status_crisis.html', {'agency':agency})

def crisis_update(request, pk, template_name='update_crisis.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    form = CrisisForm(request.POST or None, instance=crisis)
    if form.is_valid():
        form.save()
        return redirect('/loggedin')
    return render(request, template_name, {'form':form})

def crisis_toggle_active(request, pk, template_name='loggedin.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    if crisis.isActive:
            crisis.isActive = 0
    else:
            crisis.isActive = 1
    crisis.save()
    return redirect('/loggedin')


def crisis_delete(request, pk, template_name='crisis_confirm_delete.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    if request.method=='POST':
        crisis.delete()
        return redirect('/loggedin')
    return render(request, template_name, {'object':crisis})


