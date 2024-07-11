from django.shortcuts import render,redirect
from .forms import User_registration_form
# Create your views here.
def register_view(request):
    if request.method=="POST":
        form=User_registration_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    else:
        form=User_registration_form()
        context={"form":form}
        return render(request,'userauth/signup.html',context)





        