from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm, ProfileForm

# --- Login and Logout ---
class BlogLoginView(LoginView):
    template_name = 'blog/auth/login.html'
    redirect_authenticated_user = True

class BlogLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# --- Registration ---
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'blog/auth/register.html', {"form": form})

# --- Profile ---
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/auth/profile.html', {"form": form})
