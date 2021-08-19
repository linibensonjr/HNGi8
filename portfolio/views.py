from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def portfolio(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # data = {
        #     'name': fname,
        #     'email': email,
        #     'subject': subject,
        #     'message': message
        # }
        
        # message = '''
        # New message: {}

        # From: {}
        
        # '''.format(data['message'], data['email'])
        # send_mail(
        #     subject,
        #     message,
        #     email,

            
        #     ['linibensonjr@gmail.com]'])
    return HttpResponse("Hello, we got it")

    return render(request, 'index.html', {})
