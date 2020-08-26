from django.urls import path
from .views import index, by_category, book_detail_view
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'
urlpatterns = [
    path('<int:category_id>/', by_category, name="by_category"),
    path('vacancy/<int:vacancy_id>/', book_detail_view, name="vacancy"),
    path('', index, name='index'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)