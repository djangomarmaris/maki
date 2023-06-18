from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404

# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def index(request):

    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')

            message = request.POST.get('message')


            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nMessages:%s" % (
                name,
                email,

                message,
            )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

            messages.success(request, 'Teşekkürler isteğiniz tarafımıza ulaştı.')

        return redirect('/')

    return render(request,'central/index.html')