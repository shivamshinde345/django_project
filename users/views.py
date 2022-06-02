from django.shortcuts import render, redirect
from django.contrib import messages

from blog.models import crudst
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def stdisplay(request):
    results=crudst.objects.all()
    return  render(request,'blog/disp.html',{"crudst":results})
    