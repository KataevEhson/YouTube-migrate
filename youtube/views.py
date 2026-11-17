from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *





def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email']
            )
        else:
            return redirect('registration')
        return redirect('login')
    return render(request, 'registration.html')


# image = models.ImageField(upload_to='video_images/')


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username = data['username'],
            password = data['password'],
            email = data['email']
        )
        if user is not None:
            login(request, user)
            return redirect('create_video')
    return render(request, 'login.html')








@login_required
def create_video(request):
    if request.method == 'POST':
        Video.objects.create(
            user_id=request.user,
            title=request.POST['title'],
            author=request.POST['author'],
            caption=request.POST['caption'],
            category_id=Ganr.objects.get(pk=request.POST['category']),
            video=request.FILES['video'],
            image=request.FILES['image'],
        )
        return redirect('create_video')

    categories = Ganr.objects.all()
    return render(request, 'create_video.html', {'categories': categories})
