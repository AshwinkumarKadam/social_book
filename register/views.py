from django.shortcuts import render, HttpResponseRedirect
from register.forms import SignUpForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages

# signup
def sign_up(request):
    if request.method == 'POST':
        signup_fm_obj = SignUpForm(request.POST, request.FILES)
        # signup_fm_obj.password1 = request['POST']['password1']
        # signup_fm_obj.password2 = request['POST']['password2']
        if signup_fm_obj.is_valid():
            signup_fm_obj.save()
        else:
             for errors in signup_fm_obj.error_messages:

                    messages.error(request, signup_fm_obj.error_messages[errors])


    else:
        signup_fm_obj = SignUpForm()
        
    return render(request, 'register/signup.html', {'form':signup_fm_obj})

#signin
def signin(request):
        if request.method == 'POST':
            signin_fm_obj = AuthenticationForm(request=request, data=request.POST)
            if signin_fm_obj.is_valid():
                uname = signin_fm_obj.cleaned_data['username']
                upass = signin_fm_obj.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/Author_User/')
            else:
                for errors in signin_fm_obj.error_messages:

                    messages.error(request, signin_fm_obj.error_messages[errors])

        else:
            signin_fm_obj= AuthenticationForm()
            
        return render(request, 'register/login.html',{'form':signin_fm_obj})

#Author and user lists
def Author_User(request):
    Author_User_data = CustomUser.objects.all()
    context ={'a_u':Author_User_data, 'show_navigation':'True' }
    return render(request, 'register/Author_User.html',context= context)

#profiles
def Profile(request,id):
    profile_object = CustomUser.objects.get(id=id)
    if profile_object.gender == 'M':
        profile_object.gender = 'Male'
    if profile_object.gender == 'F':
        profile_object.gender = 'Female'

    context = {'show_navigation':'True', 'profile_object':profile_object}
    return render (request, 'register/Profile.html', context= context)


