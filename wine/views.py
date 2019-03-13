from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
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
from .models import WineData
# Create your views here.          
def load_file(myfile):
     fs = FileSystemStorage()
     fname = fs.save(myfile.name,myfile)
     cdir = os.path.dirname(__file__)
     path = '../media/'+fname
     p = os.path.join(cdir,path)
     f = open(p, 'r', encoding='utf8')
     reader_object = csv.reader(f)
     next(reader_object)
     for row in reader_object:
          wine_object = WineData(country = row[1],description = row[2],designation = row[3],points = row[4],price = row[5],province = row[6],region_1 = row[7],region_2 = row[8],variety = row[9],winery = row[10])
          wine_object.save()

def home(request):
     c ={}
     c.update(csrf(request))
     return render(request,'display_data.html',c)
def file_request(request):
     c ={}
     c.update(csrf(request))
     return render(request,'index.html',c)
def upload_file(request):
     c = {}
     c.update(csrf(request))
     if(request.method == 'POST'):
          myfile = request.FILES['myfile']
          thread1 = threading.Thread(target=load_file, args=(myfile,)) 
          thread1.start()
          request.session['msg'] =  "If file size is large than take time to reflect data in databse."
     return HttpResponseRedirect('/home/display_data')