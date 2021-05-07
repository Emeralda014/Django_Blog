from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy

# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm 
    template_name = 'registration/password_success.html'
    success_url = reverse_lazy('password_success')

def  password_success(request):
        return render(request, 'registration/password_success.html', {})
    
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

def get_object(self):        
    return self.request.user

class PasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')

def password_reset(request):
    return render(request, 'registration/password_reset_done.html', {})
