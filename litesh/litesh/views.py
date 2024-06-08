from time import *
from django.shortcuts import render
from win10toast import ToastNotifier
import pywhatkit as pyw

def homepage(request):
    return render(request,'index.html')

def emailgen(request):
    a = 0
    try:
        if request.method == "POST":
            namer = request.POST.get('exampleInputEmail1')
            nums = request.POST.get('exampleInputPassword1')
            a = namer + nums + "@gmail.com"
    except:
        a = "INVALID"
    return render(request,'emailgen.html',{'a':a})

def timer(request):
    try:
        if request.method == "POST":
            title = "ALERT!!!"
            mess = request.POST.get('timermessage')
            durat = eval(request.POST.get('timerduration'))
            count = eval(request.POST.get('timercount'))
            i = 0
            while i <=count:
                toaster = ToastNotifier()
                toaster.show_toast(title, mess, duration=durat)
                i+=1
                if i == count:
                    # mess: ' '
                    durat = 0
                    count = 0
                    break
            
    except:
        print("pass")
    return render(request,'timer.html')

def messanger(request):
    try:
        if request.method == "POST":
            numb = request.POST.get('number')
            message = request.POST.get('message')
            hours = eval(request.POST.get('hours'))
            minutes = eval(request.POST.get('minutes'))
            print(numb,message,hours,minutes)
            pyw.sendwhatmsg(numb,message,hours,minutes)
    except:
        print('failed')
    return render(request,'messanger.html')