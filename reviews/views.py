from django.shortcuts import render
from django.core.mail import send_mail
from .models import Reviews
from decouple import config

def place_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        Reviews.objects.create(name=name, review=review)

        subject = 'Hello from MK method!'
        message = f'Assalam-o-alakum Mehboob khan. You got a review on your method-{review}.'
        from_email = config('EMAIL_HOST_USER')
        recipient_list = [config('MAIL_TO')]

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            print("Error sending email:", e)

    try:
        all_reviews = Reviews.objects.all()
    except Exception as e:
        print("Error fetching reviews:", e)
        all_reviews = []

    return render(request, 'reviews.html', {'all_reviews': all_reviews})

def google_v(request):
    return render(request, 'google_verification.html')

