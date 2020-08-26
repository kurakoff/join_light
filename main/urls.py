from django.urls import path
from .views import index, by_category, book_detail_view

app_name = 'main'
urlpatterns = [
    path('<int:category_id>/', by_category, name="by_category"),
    path('vacancy/<int:vacancy_id>/', book_detail_view, name="vacancy"),
    path('', index, name='index'),
    ]