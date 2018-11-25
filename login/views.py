from django.shortcuts import render
from django.http import HttpResponse
from login.models import Accounts
from django.contrib import messages
from django.http import JsonResponse
import cv2
import time
import os
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
# Create your views here.
def index(request):
    if request.method=="POST":
        uup=(request.POST.get('uup'))
        bank=uup[:3]
        Id=uup[-4:]
        Id=int(Id)
        try:
            p = Accounts.objects.get(Bank=bank,Id=Id)
        except Accounts.DoesNotExist:
            messages.error(request,'Invalid Details')
        else:
            request.session['uup']=uup
            request.session['Id']=Id
            return HttpResponseRedirect('/eatm/SBI/')
            # def assure_path_exists(path):
            #     dir = os.path.dirname(path)
            #     if not os.path.exists(dir):
            #         os.makedirs(dir)
            # recognizer = cv2.face.LBPHFaceRecognizer_create()
            # assure_path_exists("trainer/")
            # recognizer.read('trainer/trainer.yml')
            # cascadePath = "haarcascade_frontalface_default.xml"
            # faceCascade = cv2.CascadeClassifier(cascadePath)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cam = cv2.VideoCapture(0)
            # timeout = 20
            # timeout_start = time.time()
            # count=0
            # while (time.time() < (timeout_start + timeout)):
            #     ret, im =cam.read()
            #     gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            #     faces = faceCascade.detectMultiScale(gray, 1.2,5)
            #     Id=0
            #     for(x,y,w,h) in faces:
            #         cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
            #         Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            #         if(Id==request.session['Id'] and (100-confidence)>55):
            #             count=count+1
            #             if(count>4):
            #                 print(Id)
            #                 print(request.session['Id'])
            #                 return HttpResponseRedirect('/eatm/home/')

            # messages.error(request,"couldn't recognize your face")
            # print("can't rec")
            # cam.release()
            # cv2.destroyAllWindows()
    return render(request,"new.html")


def auth(request):
    if request.method=='POST':
        print("ok")
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        assure_path_exists("trainer/")
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cam = cv2.VideoCapture(0)
        timeout = 20
        timeout_start = time.time()
        count=0
        while (time.time() < (timeout_start + timeout)):
            ret, im =cam.read()
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2,5)
            Id=0
            for(x,y,w,h) in faces:
                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
                Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if(Id==request.session['Id'] and (100-confidence)>55):
                    count=count+1
                    if(count>4):
                        print(Id)
                        print(request.session['Id'])
                        return JsonResponse({ 'success': True,"url":'/eatm/home/', })

        messages.error(request,"couldn't recognize your face")
        print("can't rec")
        cam.release()
        cv2.destroyAllWindows()
    return render(request,"Auth.html")


def home(request):
    print("here")
    return render(request,"home.html")
