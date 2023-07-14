from django.shortcuts import render
from django.core.mail import send_mail

def send(request):
    send_mail('EMAIL PRUEBA DJANGO',
              'Sirve :V',
              'aphoccot@unsa.edu.pe',
              ['pocochuk12345@gmail.com'],
              fail_silently=False)
    return render(request, 'email.html')