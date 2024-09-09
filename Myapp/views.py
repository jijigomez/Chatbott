from django.shortcuts import render

def index_pro(request):
    return render(request,'index_pro.html')
 
# Create your views here.

def login_page(request):
    return render(request,'login_page.html')

def register(request):
    return render(request,'register.html')
from django.http import JsonResponse
from django.shortcuts import render
from .nltk_bot import chatbot_response
from .models import Appointment
def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        specialization = request.POST.get('specialization')
        date = request.POST.get('date')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        
        print(f"User Input: {user_input}")
        print(f"Specialization: {specialization}")
        print(f"Date: {date}")
        print(f"Contact Number: {contact_number}")
        print(f"Email: {email}")
        
        user_data = {
            'specialization': specialization,
            'date': date,
            'contact_number': contact_number,
            'email': email
        }
        
        bot_response = chatbot_response(user_input, user_data)
        
        if "Your appointment with a" in bot_response:
            if specialization and date and contact_number and email:
                Appointment.objects.create(
                    specialization=specialization,
                    date=date,
                    contact_number=contact_number,
                    email=email
                )
        
        return JsonResponse({'response': bot_response})
    
    return render(request, 'chatbot.html')
