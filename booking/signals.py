from django.dispatch import Signal
from django.core.mail import EmailMessage

# Create a custom signal
custom_signal = Signal()

Subject = "Test email"
Body = "This is the test message."
# Define a function to be connected to the signal
def say_hello(sender, **kwargs):
    email = EmailMessage('Subject', 'Body', to=['nirajpatharkar21@gmail.com'])
    email.send()
    print("Hello from the custom function!")

# Connect the function to the signal
custom_signal.connect(say_hello)
