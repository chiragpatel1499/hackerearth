from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response,redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
import csv
from django.core.files.storage import FileSystemStorage
import os
import threading
from wine.models import WineData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required(login_url= '/login/')
def home(request):
    c = {}
    c.update(csrf(request))
    try:
        c['msg'] = request.session['msg']
        request.session['msg'] = ''
    except Exception as e:
        c['msg'] = ''
    return HttpResponseRedirect('display_data/',c)

@login_required(login_url= '/login/')
def display_data(request):
    c = {}
    c.update(csrf(request))
    wines = WineData.objects.all()
    c['wines'] = wines
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2
    #user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(wines, 10)
    try:
        wines_page = paginator.page(page)
    except PageNotAnInteger:
        wines_page = paginator.page(1)
    except EmptyPage:
        wines_page = paginator.page(paginator.num_pages)
    c['wines_page']=wines_page
    return render(request,'display_data.html',c)

@login_required(login_url= '/login/')
def filter_By_Country(request):
    c = {}
    c.update(csrf(request))
    arr = request.POST.getlist('check[]')
    data = []
    print(arr)
    for cn in arr:
        data += WineData.objects.filter(country = cn)
    c['wines'] = data
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2
    c['wines_page']=data
    return render(request, 'display_data.html', c)

@login_required(login_url= '/login/')
def filter_By_Province(request):
    c = {}
    c.update(csrf(request))
    arr = request.POST.getlist('check[]')
    data = []
    print(arr)
    for cn in arr:
        data += WineData.objects.filter(province = cn)
    c['wines'] = data
    wines=data
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2 
    c['wines_page']=data
    return render(request, 'display_data.html', c)

@login_required(login_url= '/login/')
def filter_By_Region_1(request):
    c = {}
    c.update(csrf(request))
    arr = request.POST.getlist('check[]')
    data = []
    print(arr)
    for cn in arr:
        data += WineData.objects.filter(region_1 = cn)
    c['wines'] = data
    wines=data
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2
    c['wines_page']=data
    c['wines_page']=wines
    return render(request, 'display_data.html', c)

@login_required(login_url= '/login/')
def filter_By_Region_2(request):
    c = {}
    c.update(csrf(request))
    arr = request.POST.getlist('check[]')
    print(arr)
    data = []
    for cn in arr:
        data += WineData.objects.filter(region_2 = cn)
    c['wines'] = data
    wines=data
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2
    c['wines_page']=data
    c['wines_page']=wines
    return render(request, 'display_data.html', c)

def sort_column(request):
    c = {}
    c.update(csrf(request))
    param = request.GET.get('param')
    if param == 'id':
        wines = WineData.objects.order_by('id')
    elif param == 'country':
        wines = WineData.objects.order_by('country')
    elif param == 'description':
        wines = WineData.objects.order_by('description')
    elif param == 'designation':
        wines = WineData.objects.order_by('designation')
    elif param == 'points':
        wines = WineData.objects.order_by('points')
    elif param == 'price':
        wines = WineData.objects.order_by('price')
    elif param == 'province':
        wines = WineData.objects.order_by('province')
    elif param == 'region_1':
        wines = WineData.objects.order_by('region_1')
    elif param == 'region_2':
        wines = WineData.objects.order_by('region_2')
    elif param == 'variety':
        wines = WineData.objects.order_by('variety')
    elif param == 'winery':
        wines = WineData.objects.order_by('winery')
    else:
        wines = WineData.objects.all()
    c['wines'] = wines
    c['wines_page']=wines
    countries = WineData.objects.values('country').distinct().order_by('country')
    c['countries'] = countries
    province = WineData.objects.values('province').distinct().order_by('province')
    c['province'] = province
    region_1 = WineData.objects.values('region_1').distinct().order_by('region_1')
    c['region_1'] = region_1
    region_2 = WineData.objects.values('region_2').distinct().order_by('region_2')
    c['region_2'] = region_2
    return render(request, 'display_data.html', c)
