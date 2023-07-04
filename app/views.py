from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first(request):
    if request.method == 'POST':
        topic= request.POST['tn']

        TO = Topic.objects.get_or_create(topic_name = topic)[0]
        TO.save()
        return HttpResponse('topi_name is submited')
    


    return render(request,'first.html')

def insert_webpages(request):
    TO = Topic.objects.all()
    d = {'TO':TO}
    if request.method == 'POST':
        topic= request.POST['wb']
        TO = Topic.objects.get(topic_name=topic)
        TO.save()
        name = request.POST['un']
        url = request.POST['ur']

        WO = Webpage.objects.get_or_create(topic_name= TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('Webpage is submited')
    return render(request,'insert_webpages.html',d)


def insert_access(request):
    if request.method == 'POST':
        name = request.POST['uo']
        WO = Webpage.objects.get(name=name)
        WO.save()
        date = request.POST['dt']
        author = request.POST['ar']
        AO = AccessRecord.objects.get_or_create(name = WO, date = date,author = author )[0]
        AO.save()
        return HttpResponse('access recodes is submited')
    return render(request,'insert_access.html')

def retrieve_webpages(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    if request.method == 'POST':
        MSTS = request.POST.getlist('tn')
        wos = Webpage.objects.none()
        for i in MSTS:
            wos = wos | Webpage.objects.filter(topic_name = i)
        d1 = {'wos': wos}
        return render(request,'display_webpages.html',d1)
    return render(request,'retrieve_webpages.html',d)

def checkbox(request):
    LTO = Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'checkbox.html',d)
