from django.shortcuts import render,redirect,get_object_or_404
from .models import User
import datetime
def home(request):
        if request.method == "POST":
                email = request.POST.get('email')
                password = request.POST.get('password')
                print('email:', email)
                print('password:', password)
                user = User.objects.filter(email=email, password=password).first()  # Dummy authentication logic for demonstration
                if user:
                    return render(request,'user_home.html',{'user':user})  
                else:
                    return render(request, 'index.html', {'error': 'Invalid email or password.'})
        return render(request, 'index.html')

def user_signup(request):
       if request.method == "POST":
             username = request.POST.get('username')
             dob = request.POST.get('dob')
             email = request.POST.get('email')
             password = request.POST.get('password')
             try:
                dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
             except (ValueError, TypeError):
                return render(request, 'signup.html', {'error': 'Invalid date of birth format.'})
             print('username:', username)
             print('dob:', dob)
             print('email:', email)
             print('password:', password)
             if User.objects.filter(email=email).exists():
                   return render(request, 'signup.html', {'error': 'Email already exists! Try another one.'})
             User.objects.create(
                   username=username,
                   date_of_birth=dob,
                   email=email,
                   password=password,
                   user_type=1  
             )
             return redirect('home')
       return render(request,'signup.html')
          