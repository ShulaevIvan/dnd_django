from django.shortcuts import redirect, render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }

        return render(request, self.template_name, context)

    def post(self, request):

        form = UserCreationForm(self.request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)

            return redirect('home')

        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)


class Account(View):

    def get(self, request):

        template_name = 'account.html'
        context = {}

        return render(request, template_name, context)



