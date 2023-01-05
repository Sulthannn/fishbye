from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    kelola =  Tangkap.objects.all()
    tipe =  Nelayan.objects.all()
    data = {
       'kelola' : kelola,
       'tipe' : tipe,
    }
    return render(request, 'index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def halamantangkapan(request):
    kelola =  Tangkap.objects.all()
    data = {
       'kelola' : kelola, 
    }
    return render(request, 'halamantangkapan.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahtangkapan(request):
    if request.POST:
        form = FormTangkap(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormTangkap()
            kelola = Tangkap.objects.all()
            data = {
            'kelola' : kelola,
            'form'  : form,
            }
            return render(request, 'tambahtangkapan.html', data)
    else:
        form = FormTangkap()
        kelola = Tangkap.objects.all()
        data = {
           'kelola' : kelola,
           'form'  : form,
        }
    return render(request, 'tambahtangkapan.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updatetangkapan(request, id):
    ubahtangkap = Tangkap.objects.get(pk=id)
    if request.POST:
        if request.FILES:
            ubahtangkap.gambar.delete()
        form = FormTangkap(request.POST, request.FILES, instance=ubahtangkap)
        if form.is_valid():
            form.save()
            data = {  
                'tangkap' : ubahtangkap,
                'form'  : form,
            }
            return render(request, 'updatetangkapan.html', data)
    else:
        form = FormTangkap(instance=ubahtangkap)
        data = {
        'tangkap' : ubahtangkap,
        'form'  : form,
        }
    return render(request, 'updatetangkapan.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deletetangkapan(request, id):
    tangkap = Tangkap.objects.get(pk=id)
    tangkap.gambar.delete()
    tangkap.delete()
    
    return redirect("/halamantangkapan/")


@login_required(login_url=settings.LOGIN_URL)
def halamanadmin(request):
    tipe =  Nelayan.objects.all()
    data = {
        'tipe' : tipe,
    }
    return render(request, 'halamanadmin.html', data)


@login_required(login_url=settings.LOGIN_URL)
def tambahnelayan(request):
    if request.POST:
        form = FormNelayan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormNelayan()
            tipe = Nelayan.objects.all()
            data = {
            'tipe' : tipe,
            'form'  : form,
            }
            return render(request, 'tambahnelayan.html', data)
    else:
        form = FormNelayan()
        tipe = Nelayan.objects.all()
        data = {
           'tipe' : tipe,
           'form'  : form,
        }
    return render(request, 'tambahnelayan.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updatenelayan(request, qr):
    ubahnelayan = Nelayan.objects.get(pk=qr)
    if request.POST:
        if request.FILES:
            ubahnelayan.gambar.delete()
        form = FormNelayan(request.POST, request.FILES, instance=ubahnelayan)
        if form.is_valid():
            form.save()
            data = {  
                'nelayan' : ubahnelayan,
                'form'  : form,
            }
            return render(request, 'updatenelayan.html', data)
    else:
        form = FormNelayan(instance=ubahnelayan)
        data = {
        'nelayan' : ubahnelayan,
        'form'  : form,
        }
    return render(request, 'updatenelayan.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deletenelayan(request, qr):
    nelayan = Nelayan.objects.get(pk=qr)
    nelayan.gambar.delete()
    nelayan.delete()
    
    return redirect("/halamanadmin/")


def registrasi(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Berhasil Dibuat!")
            return redirect('registrasi')
        else:
            messages.error(request, "Gagal Dibuat!")
            return redirect('registrasi')
    else:
        form = UserCreationForm()
        data = {
            'form':form,
        }
    return render(request, 'registrasi.html', data)