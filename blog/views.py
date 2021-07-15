from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from blog.models import topic,text,accessDate
#####################
from blog.forms import NewUserForm,UserForm,UserProfileInfoForm
#####################
from . import forms
#########      login #####################################
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
##########################################################
def user(request):
    form=NewUserForm
    if request.method == "POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ValidationError')
            return render(request,'blog/user.html',{'form':form})
    return render(request,'blog/user.html',{'form':form})


def register_user(request):
    registerd=False
    if request.method== 'POST':
        user_form=UserForm
        profile_form=UserProfileInfoForm
        user_form=user_form(request.POST)
        profile_form=UserProfileInfoForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registerd= True
            return render(request,'blog/user_register.html',{'user_form':user_form,'profile_form':profile_form,
            'registerd':registerd,})


        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
        return render(request,'blog/user_register.html',{'user_form':user_form,'profile_form':profile_form,
        'registerd':registerd,})



def base(request):
    return render(request, 'blog/base.html')



########################################################
@login_required
def home(request):
    content=text.objects.order_by('id')
    side_bar=topic.objects.order_by('id')
    data={'title':'Welcome to Django','content':content,'side_bar':side_bar}
    return render(request, 'blog/home.html', context=data)


########################################################
def add_text(request):
    from django.core.files.storage import FileSystemStorage
    form=forms.add_text()
    if request.method=='POST':
        form=forms.add_text(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file=request.FILES['file']
            print("Validtion Success ")
            print(form.cleaned_data['title'])
            print(form.cleaned_data['text'])
            print(uploaded_file.name)
            print(uploaded_file.size)
            fs=FileSystemStorage
            fs.save(uploaded_file.name, uploaded_file)


    return render(request,'blog/add_text.html',{'form':form})


########################################################
def register(request):
    form=forms.registration()
    return render(request,'blog/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect('/blog/')
                return HttpResponseRedirect(reverse('blog:Home'))
            else:
                return HttpResponse('Account is not Active')
        else:
            return HttpResponse('Invalid username or Password')
    else:
        form=forms.user_login()
        return render(request, 'blog/login.html', {'form':form})
