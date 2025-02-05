from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login

def BASE(request):
    return render(request,"base.html")
def LOGIN(request):
    return render(request,"login.html")


def doLogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=EmailBackEnd.authenticate(request,username=email,password=password)
        if user!=None:
            login(request, user)
            user_type=user.user_type
            if user_type=='1':
                return HttpResponse("hod")
            elif user_type=='2':
                return HttpResponse("staff")
            elif user_type=='3':
                return HttpResponse("student")
            else:
                # Message
                return redirect(LOGIN)
        else:
            # Message
            return redirect(LOGIN)