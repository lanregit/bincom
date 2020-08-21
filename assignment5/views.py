from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from assignment5.forms import Invites, Contact, UserComment
from assignment5.models import Category, Post, Comments, Pictures, Video
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'assignment5/index.html')


def our_story(request):
    return render(request, 'assignment5/our_story.html')


def location(request):
    return render(request, 'assignment5/location.html')


def gallery(request):
    pic = Pictures.objects.all()
    vid = Video.objects.all()
    args = {'pic':pic, 'vid':vid}
    return render(request, 'assignment5/gallery.html', args)


def booking(request):
    if request.method == 'POST':
        form = Invites(request.POST)
        if form.is_valid:
            form.save(commit=True)
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            guest = form.cleaned_data['guest']
            from_email = settings.EMAIL_HOST_USER
            message = '{} has filled invitation form {}'.format(name, guest)
            send_mail('New Guest', message, email, ['muyi2010@yahoo.com'])
            return HttpResponse('Invitation Received! Thank you')
    else:
        form = Invites()
    return render(request, 'assignment5/booking.html', {'form':form})


def contact(request):
    contactform = Contact()
    return render(request, 'assignment5/contact.html', {'contactform':contactform})


def blog(request):
    post = Post.objects.all()
    return render(request, 'assignment5/blog.html', {'post':post})


def blog_details(request, pos_id):
    pol = Post.objects.get(id=pos_id)
    comments = Comments.objects.filter(post=pol).order_by('time')
    if request.method == 'POST':
        com = UserComment(request.POST)
        if com.is_valid:
            com_s = com.save(commit=False)
            com_s.post = pol
            com_s.comment_by = request.user 
            com.save(commit=True)
            return HttpResponseRedirect(request.path_info)
    else:
        com = UserComment(request.POST)    
    return render(request, 'assignment5/single-blog.html', {'pol':pol, 'com':com, 'comments':comments})

def element(request):
    return render(request, 'assignment5/elements.html')

