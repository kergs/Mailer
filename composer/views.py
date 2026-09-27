from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import EmailForm
import logging
logger = logging.getLogger(__name__)

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            from_email = f"{data['from_local_part']}@lukoil.com"
            email = EmailMessage(
                subject=data['subject'],
                body=data['body'],
                from_email=from_email,
                to=[e.strip() for e in data['to'].split(',')],
                cc=[e.strip() for e in data['cc'].split(',')] if data['cc'] else [],
                bcc=[e.strip() for e in data['bcc'].split(',')] if data['bcc'] else [],
                reply_to=[data['reply_to']] if data['reply_to'] else None,
            )
            if data['attachment']:
                email.attach(
                    data['attachment'].name,
                    data['attachment'].read(),
                    data['attachment'].content_type
                )
            email.send()
            return redirect('send_email')
    else:
        form = EmailForm()
    return render(request, 'composer/send_email.html', {'form': form})