from django.shortcuts import render
from .models import Vacancie, Сategory
from django. http import HttpResponse, Http404
from django.template import TemplateDoesNotExist

# Create your views here.
def index(request):
    vacancies = Vacancie.objects.all()
    categories = Сategory.objects.all()
    context = {'vacancies': vacancies, 'categories':categories}
    return render(request, 'main/index.html', context)

def by_category(request, category_id):
    vacancies = Vacancie.objects.filter(category=category_id)
    categories = Сategory.objects.all()
    current_category = Сategory.objects.get(pk=category_id)
    context = {'vacancies': vacancies, 'categories': categories, 'current_category':current_category}
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