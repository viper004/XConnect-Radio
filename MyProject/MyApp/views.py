from django.shortcuts import render,redirect,get_object_or_404
from . import models

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        xconnect_number = request.POST.get('xconnect-number')
        print(username,xconnect_number)
        if username and xconnect_number:
           
            return redirect('chat')
        else:
            models.ChatUser.objects.create(
                username=username, 
                xconnect_number=xconnect_number
                )
            return render(request, 'index.html', {'error': 'Please enter both username and XConnect number.'})
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')