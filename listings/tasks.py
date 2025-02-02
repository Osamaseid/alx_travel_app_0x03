from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Hello, your booking has been confirmed!\n\nDetails:\n{booking_details}"
    from_email = "noreply@alxtravel.com"
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
