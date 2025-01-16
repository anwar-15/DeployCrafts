from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, requires_csrf_token
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
# Create your views here.

def IndexView(request):
    return render(request, 'authenticate/home.html')


@login_required
def DashboardView(request, username):
    if request.user.username != username:
        # Prevent access to another user's dashboard
        return render(request, '403.html', status=403)

    return render(request, 'authenticate/dashboard.html', {'username': username})

@csrf_protect
@requires_csrf_token
def RegisterView(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "You are successfully registered!!!")
            return HttpResponseRedirect(reverse('authenticate:home'))
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            return render(request, 'authenticate/register.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'authenticate/register.html', {'form':form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'authenticate/login.html'
    #redirect_authenticated_user = True
    def get_success_url(self):
        # Redirect to a user-specific dashboard
        return reverse('authenticate:dashboard', kwargs={'username': self.request.user.username})


class CustomLogoutView(LogoutView):
    template_name = 'authenticate/logout.html'





