from django.shortcuts import render
from django.core.mail import send_mail
from .models import Reviews
from decouple import config

def place_review(request):
    if request.method=='POST':
        name=request.POST.get('name')
        review=request.POST.get('review')
        Reviews.objects.create(name=name,review=review)
        subject = 'Hello from MK method!'
        message = f'Assalam-o-alakum Mehboob khan. You got a review on your method-{review}.'
        from_email = config('EMAIL_HOST_USER')
        recipient_list = [config('MAIL_TO')]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    all_reviews=Reviews.objects.all()
    return render(request,'reviews.html',{'all_reviews':all_reviews})