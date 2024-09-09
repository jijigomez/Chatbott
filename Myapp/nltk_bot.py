from nltk.chat.util import Chat, reflections
from .models import Appointment  # Import your model

# Define pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1,Please provide Email ",]
    ],
    [
        r"I want to book an appointment",
        ["Sure, which specialization are you looking for? We have Cardiology, Dermatology, Orthopedics, Pediatrics, and more.",]
    ],
    [
        r"I need a (.*) appointment",
        ["Great! You have selected %1. When would you like to schedule your appointment?",]
    ],
    [
        r"book appointment on (.*) for (.*)",
        ["Your appointment with a %2 specialist is booked for %1. Please provide your contact number.",]
    ],
    [
        r"My contact number is (.*)",
        ["Thanks for providing your contact number: %1. We will send you a confirmation shortly. Please provide your email.",]
    ],
    [
        r"My email is (.*)",
        ["Your email %1 has been recorded. We will send all details to this address.",]
    ],
    [
        r"thank you",
        ["You're welcome! Have a great day!",]
    ]
]

# Create chatbot
appointment_chatbot = Chat(pairs, reflections)

def chatbot_response(user_input, user_data):
    response = appointment_chatbot.respond(user_input)
    
    # Save user data to the database
    if "Your appointment with a" in response:
        specialization = user_data.get('specialization')
        date = user_data.get('date')
        contact_number = user_data.get('contact_number')
        email = user_data.get('email')
        
        if specialization and date and contact_number and email:
            Appointment.objects.create(
                specialization=specialization,
                date=date,
                contact_number=contact_number,
                email=email
            )
    
    return response
