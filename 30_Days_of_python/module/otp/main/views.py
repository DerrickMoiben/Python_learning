from django.shortcuts import render, redirect
from random import randint, choice
import string
from .forms import signupForm
from .models import Signup
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'home.html')


def otp_generate():
    randomstr = ""
    for i in range(1, 4):
        digits = randint(0, 7)
        alphanumeric = choice(string.ascii_letters)
        randomstr += str(digits) + alphanumeric

    return randomstr

otp = otp_generate()


def signup(request):
    if request.method  == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')

            # send email
            subject = 'Email Verification'
            message = f'Your OTP is below: use it to verify your email.'  # Correctly defined as a string
            html_message = f"""
                <html>
                    <body>
                        <h1>OTP Verification</h1>
                        <p>Dear {user.name},</p>
                        <p>Your OTP is: <strong>{otp}</strong></p>
                    </body>
                </html>
                """

            send_mail(
                    subject,                     # Subject of the email
                    message,                     # Plain text fallback
                    'derrickmoio92@gmail.com',   # Sender's email
                    [email],                     # Recipient's email
                    fail_silently=False,         # Raise errors if any
                    html_message=html_message,  # HTML content of the email
                )

            
            return redirect('verifyotp')
    else:
        form = signupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def all_users(request):
    users = Signup.objects.all()
    context = {'users': users}
    return render(request, 'all_users.html', context)

def delete_user(request, pk):
    user = Signup.objects.get(id=pk)
    user.delete()
    return redirect('all_users')


from django.contrib import messages

def verifyotp(request):
    if request.method == 'POST':
        otp_entered = request.POST['otp']
        if otp_entered == otp:
            return redirect('home')
        else:
            messages.error(request, 'Enter the correct OTP') 
            return redirect('verify_otp')
    return render(request, 'verify_otp.html')


