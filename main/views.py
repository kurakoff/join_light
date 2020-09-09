from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Vacancie, Сategory, Subcategory
from django.http import HttpResponse, Http404, BadHeaderError, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from .forms import ContactForm

# Create your views here.
def index(request):
    vacancies = Vacancie.objects.all()
    categories = Сategory.objects.all()
    count_vacancies = Vacancie.objects.all().count()
    context = {'vacancies': vacancies, 'categories':categories, 'count_vacancies':count_vacancies}
    return render(request, 'main/index.html', context)

def by_category(request, category_id):
    vacancies = Vacancie.objects.filter(category=category_id)
    categories = Сategory.objects.all()
    count_vacancies = Vacancie.objects.filter(category=category_id).count()
    current_category = Сategory.objects.get(pk=category_id)
    context = {'vacancies': vacancies, 'categories': categories, 'current_category':current_category,'count_vacancies':count_vacancies}
    return render(request, 'main/by_category.html', context)


def book_detail_view(request, vacancy_id):
    try:
        vacancy = Vacancie.objects.get(pk=vacancy_id)
        categories = Сategory.objects.all()
    except Vacancie.DoesNotExist:
        raise Http404("Vacancy does not exist")

    return render(
        request,
        'main/vacancy_detail.html',
        context={'vacancy': vacancy, 'categories': categories,}
    )

# Функция формы обратной связи
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            new = form.cleaned_data['new']
            copy = form.cleaned_data['copy']

            recepients = ['sizze.team@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'sizze.team@gmail.com', recepients, html_message="Доп"+new)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('thanks')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'forms/contact.html', {'form': form, 'username': auth.get_user(reguest).username})

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'forms/thanks.html', {'thanks': thanks})


