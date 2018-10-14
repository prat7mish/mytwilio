

# Create your views here.
from django.shortcuts import render,redirect
from twilio.rest import Client
from twiliobydjango import settings
from .forms import PostModelForm,PostForm
from django.http import HttpResponse
from twilio.base.exceptions import TwilioRestException
import random

g_pin=0
def pin_gen():
    pin = random.randint(999, 9999)
    g_pin=pin
    print(g_pin)
    return pin

def home(request):
    try:

        if request.method == "POST":
            form = PostModelForm(request.POST)
            if form.is_valid():
                global g_pin
                # commit=False means the form doesn't save at this time.
                # commit defaults to True which means it normally saves.
                
                to_num=form.cleaned_data["number"]
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                pin=pin_gen()
                print(pin)
                g_pin=pin
                message = client.messages.create(to=to_num, from_='+18327722414', body='Your verification code is %s'%str(pin))
                print(message.sid)
                

                #if form.has_error:
                #    html = "<html><body>It is now</body></html>"
                #    return HttpResponse(html)
                
                return redirect('/send/')
        else:
            form=PostModelForm()
            return render(request, "first/index.html", {'form': form})
    except TwilioRestException:
        html = "<html><body>Oops, exception encountered:Only the registered Mobile numbers can be verified in Twilio Trial Version</body></html>"
        return HttpResponse(html)
    
    

    

def sms(request):
    if request.method=="POST":
        form1=PostForm(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data["Enter_Otp"]
            print("mypin")
            print(data1)
            print("gpin")
            print(g_pin)
            if int(data1)==int(g_pin):
                
                html = "<html><body><h3>Successfully verified</h3></body></html>"
                
            else:
                html = "<html><body><h3>Please enter the Correct OTP</h3><a href="">Go back</a></body></html>"
            return HttpResponse(html)
            
    else:
        form1=PostForm()
        
        return render(request,"first/verify.html",{"form":form1})
            
        

    