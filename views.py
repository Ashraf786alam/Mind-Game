from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
import random
from .models import User
# Create your views here.
@login_required(login_url="/Quiz/login/")
def homepage(request):
    if 'login' not in request.session:
        return HttpResponseRedirect('/Quiz/Login/')
    else:
        if request.method=="GET" and request.GET.get('dummy2')=="20":
            number1=request.GET.get('number1')
            number2=request.GET.get('number2')
            number3=request.GET.get('number3')
            print("ashraf ashraf ashraf ashraf ashraf ashraf ")
            print(number1,number2,number3)
            if number3==request.session.get('answer'):
                user=User.objects.get(email=request.session['user_email'])
                #score=request.session.get('score');
                score=user.score
                score=score+1
                request.session['score']=score
                print(score)
                user.email=request.session['user_email']
                user.password=request.session['user_password']
                user.username=request.session['user_username']
                user.score=score
                user.save()
                return HttpResponse('true')
            else:
                return HttpResponse('false')
        else:
            if request.session['action']=="ADDITION":
                num1=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                num2=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                time=request.session['deadline']
                return render(request,'Quiz/home.html',{'num1':num1,'num2':num2,'time':time,'action_add':request.session['add'],'username':request.session['user_username'],'score':request.session.get('score')})
            if request.session['action']=="SUBSTRACTION":
                num1=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                num2=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                time=request.session['deadline']
                return render(request,'Quiz/home.html',{'num1':num1,'num2':num2,'time':time,'action_sub':request.session['subs'],'username':request.session['user_username'],'score':request.session.get('score')})
            if request.session['action']=="MULTIPLICATION":
                num1=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                num2=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
                time=request.session['deadline']
                return render(request,'Quiz/home.html',{'num1':num1,'num2':num2,'time':time,'action_multiply':request.session['multiply'],'username':request.session['user_username'],'score':request.session.get('score')})


def Answerpage(request):
    try:
        if request.method=="GET" and request.GET.get('dummy')=="10":
            answer=request.GET['answer']
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(answer)
            request.session['answer']=answer
            return HttpResponse('true')
    except:
        num1=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
        num2=random.randint(int(request.session['firstnumber']),int(request.session['secondnumber']))
        return render(request,'Quiz/home.html',{'num1':num1,'num2':num2,'action_add':request.session['add'],'username':request.session['user_username'],'score':request.session.get('score')})

def signuppage(request):
    if request.method=="GET" and request.GET.get('d')=="10":
        username=request.GET.get('username')
        email=request.GET.get('email')
        password=request.GET.get('password')
        print(username,email,password)
        user=User(username=username,email=email,password=password)
        user.save()
        return HttpResponse('true')
    return render(request,'Quiz/signup.html')

def Emailcheckpage(request):
    if request.method=="GET":
        email=request.GET.get('email')
        print(email)
        user=User.objects.filter(email=email)
        if user:
            return HttpResponse('true')
        else:
            return HttpResponse('false')

def loginpage(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        user=User.objects.filter(email=email)
        if user:
            if user[0].password==password:
                request.session['user_email']=email
                request.session['user_password']=password
                request.session['user_username']=user[0].username
                request.session['score']=user[0].score
                request.session['login']="login"
                return HttpResponseRedirect('/Quiz/start/')
        else:
            msg="Username or Password Invalid"
            return render(request,'Quiz/login.html',{'msg':msg})
    return render(request,'Quiz/login.html')


def startpage(request):
    if request.method=="POST":
        firstno=request.POST['firstnumber']
        secondno=request.POST['secondnumber']
        deadline=request.POST.get('deadline')
        action=request.POST['action']
        request.session['firstnumber']=firstno
        request.session['secondnumber']=secondno
        request.session['deadline']=deadline
        request.session['action']=action
        if request.session['action']=="ADDITION":
            request.session['add']='+'
        if request.session['action']=="SUBSTRACTION":
            request.session['subs']='-'
        if request.session['action']=="MULTIPLICATION":
            request.session['multiply']='x'
        print(firstno,secondno,deadline,action)
        return HttpResponseRedirect('/Quiz/home/')
    if 'login' in request.session:
        return render(request,'Quiz/start.html')
    else:
        return HttpResponseRedirect('/Quiz/Login/')

def logoutpage(request):
    request.session.clear();
    return HttpResponseRedirect('/Quiz/Login/')
