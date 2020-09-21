from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


from .forms import LoginForm


def user_login(request):
    """ Функция входа пользователя в систему """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Успешная авторизация')
            else:
                return HttpResponse('Ваши права на доступ устарели')
        else:
            return HttpResponse('Неверно указаны данные  ')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
