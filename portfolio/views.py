from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from portfolio.forms import contactMe


# Create your views here.
def portfolio(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        form = contactMe(request.POST)
        if form.is_valid():
            print('failed')
            #return redirect('index')
            return HttpResponse("Hello, we got it")
    else:
        #form = contactMe()
        print('failed')
            
        #     ['linibensonjr@gmail.com]'])
        

    return render(request, 'index.html', {'form':form})
