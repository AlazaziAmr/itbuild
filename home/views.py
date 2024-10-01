from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import Section
from django.core.mail import send_mail
from .forms import ContactFrom
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.views.decorators.cache import cache_control



# Create your views here.
def index(request):
    data = get_object_or_404(Section)
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            send_mail(subject=request.POST.get('subject'),
                      message=request.POST.get('message'),
                      from_email=request.POST.get('name') + '<' + request.POST.get('email') + '>',
                      recipient_list=['contact@itbuildyemen.com'])
            messages.success(request, _("Your message has been sent. Thank you!"), extra_tags='success')
            return redirect('home')
        else:
            messages.warning(request, _("Fail to send, check your data!!"), extra_tags='warning')
            return render(request, 'index.html', {'data': data, 'form': form}, )
    else:
        form = ContactFrom()
        return render(request, 'index.html', {'data': data, 'form': form})
    