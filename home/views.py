# from cgitb import html
from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is the view by prince")
    # passing arguments to hello .html
    context = {'name':'Prince',
                'course':'BCA'
    }
    return render(request,'home.html',context)

def control(request):
    # return HttpResponse("this is the control view by prince")
    return render(request,'projects.html')

def contact(request):

    # return HttpResponse("hii this a contact page")
    if request.method == "POST":
        # print("this is post")
        name = request.POST['naame']
        email = request.POST['email']
        addr = request.POST['addr']
        phone = request.POST['phone']
        desc = request.POST['explain']
        # print(name,email,addr,phone,desc)
        ins = Contact(name = name, email = email, addr= addr, phone = phone, desc = desc)
        ins.save()
        print("the data has been written to the db")

    return render(request, 'contact.html')

def about(request):
    # return HttpResponse("this is a about page")
    return render(request,'about.html')
