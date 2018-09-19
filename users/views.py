from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.validators import validate_email
from .models import Email

def index(request):
    return render(request, 'users/index.html')

def create_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            if email_is_valid(form.cleaned_data['email']):
                new_email = form.save()
                return redirect('emails_list')
            else:
                return render(request, 'users/create.html', {'error': 'Please enter a valid emails address', 'form': form})
        return render(request, 'users/create.html')
    else:
        form = EmailForm()
        return render(request, 'users/create.html', {'form': form})

def emails_list(request):
    emails = Email.objects.all()
    return render(request, 'users/emails_list.html', {'emails': emails})

def email_is_valid(email):
    try:
        validate_email(email)
        valid = True
    except:
        valid = False
    return valid