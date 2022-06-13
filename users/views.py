from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

from .models import User
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
            user_obj = User.objects.all().filter(email=email)
            login(request, user)
            for i in user_obj:
                Token.objects.create(user=i)
            return redirect('home')
        
        context = {
            'form': form,
        }
        
        return render(request, self.template_name, context)


class Account(View):

    def get(self, request):

        token_obj = Token.objects.all().filter(user=request.user)

        template_name = 'account.html'
        context = {
            'token': token_obj
        }

        return render(request, template_name, context)



