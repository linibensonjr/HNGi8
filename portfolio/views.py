from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from portfolio.forms import contactMe


# Create your views here.
def portfolio(request):
    form = contactMe()
    if request.method == 'POST':
        form = contactMe(request.POST)

        if form.is_valid():
            #return redirect('portfolio')
            return HttpResponse("Hello, we got it")

    return render(request, 'index.html', {'form':form})
