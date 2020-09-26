from django.shortcuts import render, redirect
from Main.models import News,Register, Mail
from .forms import AddNews_Form, EditNews_Form,RegisterForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings


#HOME PAGE SECTION!!!
def Homepage(request):
    news = News.objects.filter(valid=True)
    form = RegisterForm()
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    context = {'news': news,'form':form}
    return render(request, 'index.html', context)


#BLOG PAGE SECTION
def Blog(request):
    return render(request, 'blog.html')


#GALLERY SECTION
def Gallery(request):
    return render(request, 'gallery.html')


#CONTACT SECTION
def Contact(request):
    return render(request, 'contact.html')

def SendEmail(email, msg):
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    #html = get_template("mail.html").render({"msg": msg})
    sub = "You have got a new Email from {}".format(from_email)
    #send_mail(sub, " ", from_email, to_email, html_message=html)
    send_mail(sub, msg , from_email, to_email, fail_silently=False,)


def Contacted_Mail(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["comment"]
        print(name)
        print(email)
        Mail.objects.create(name=name, email=email, msg=message)
        msg = "Hi, {name}! Thank you for contacting us. We will answer your query within 48 hours.".format(name=name)
        SendEmail(email, msg)
    return render(request, 'contact.html')




#NEWS SECTION

def News_view(request):
    if request.user.is_authenticated:
        news = News.objects.filter(valid=True)
        students=Register.objects.all()
        mails = Mail.objects.all()
        form = AddNews_Form()
        context = {'news': news, 'form': form ,'students':students, 'mails':mails}
        return render(request, 'news.html', context)
    else:
        return render(request, 'login.html')


def Add_News(request):
    if request.method == 'POST':
        form = AddNews_Form(request.POST)
        if form.is_valid():
            t = request.POST["title"]
            try:
                vi = request.POST["valid"]
                if vi == 'on':
                    v = True
            except:
                v = False
            News.objects.create(title=t, valid=v)
    return redirect("news")


def Delete_News(request, id):
    n = News.objects.get(id=id)
    n.delete()
    return redirect("news")

def Delete_Mails(request, id):
    n = Mail.objects.get(id=id)
    n.delete()
    return redirect("news")


def Delete_Demo_users(request, id):
    n = Register.objects.get(id=id)
    n.delete()
    return redirect("news")

#ERROR SECTION
def error_404_view(request, exception):
    return render(request, '404.html')








