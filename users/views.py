from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import User, UserTokens
from .forms import UserCreationForm
from django.contrib.sessions.models import Session


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
            token = Token.objects.create(user = user_obj[0])
            UserTokens.objects.create(user=user_obj[0], token=token)

            return redirect('home')
        
        context = {
            'form': form,
        }

        response = render(request, self.template_name, context)
        
        return response
        


class Account(View):

    def get(self, request):

        token_obj = Token.objects.all().filter(user=request.user)
        template_name = 'account.html'

        context = {
            'token': token_obj
        }

        resopnse = render(request, template_name, context)
        
        return resopnse



