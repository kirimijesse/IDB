from django.shortcuts import render

# Create your views here.
path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),