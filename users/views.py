from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from users.forms import SignUpForm
from django.contrib.auth import login, authenticate


# Create your views here.
#path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
#path('password-changedone/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

class HomePageView(TemplateView):
	template_name = 'home.html'

def signup(request):
	template_name = 'signup.html'
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password= raw_password)
			login(request, user)
			return redirect('home')

	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form' : form})
