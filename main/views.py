from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Vacancie, Сategory, Subcategory
from django.http import HttpResponse, Http404, BadHeaderError, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from .forms import ContactForm
from django.template.loader import get_template

####
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.views.generic.edit import CreateView

from .models import AdvUser
from .forms import ChangeUserInfoForm

from django.contrib.auth.views import PasswordChangeView

from .forms import RegisterUserForm
from django.views.generic.base import TemplateView


from django.core.signing import BadSignature
from .utilities import signer


from django.views.generic.edit import DeleteView
from django.contrib.auth import logout
from django.contrib import messages
#Прочие страницы
def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

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
            copy = form.cleaned_data['copy']

            recepients = ['sizze.team@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'sizze.team@gmail.com', recepients)
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

#######
#Профиль вход
class JobLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def profile(request):
    return render(request, 'registration/profile.html')

#Профиль выход
class JobLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'main:index'
  # template_name = 'registration/logout.html'
   #success_url = 'main:index'

#Редактирование профиля
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView) :
    model = AdvUser
    template_name = 'registration/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile_change')
    success_message = "Changed"

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
#Смена пароля
class JobPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_changed.html'
    success_url = reverse_lazy('main:password_change')
    success_message = 'password changed'

#Регистрация
class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'registration/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'registration/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'registration/user_is_activated.html'
    else:
        template = 'registration/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name='registration/delete_user.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                           'User delated')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


