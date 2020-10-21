from django.shortcuts import render
from .models import Register

def index(request):

    if request.method == "POST":

        name = request.POST.get('name', '')

        email = request.POST.get('email', '')

        phone = request.POST.get('phone', '')

        ro = request.POST.get('ro', '')

        desc = request.POST.get('desc', '')

        r = Register(Fullname=name,Email=email,Phone=phone,Gender=ro,Desc=desc)
        r.save()

        print(name, email, phone, ro, desc)

    return render (request,'app1/index.html')
