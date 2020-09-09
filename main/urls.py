from django.conf.urls import url
from django.urls import path

from . import views
from .views import index, by_category, book_detail_view
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'
urlpatterns = [
    path('<int:category_id>/', by_category, name="by_category"),
    path('vacancy/<int:vacancy_id>/', book_detail_view, name="vacancy"),
    path('', index, name='index'),
    url(r'^contact/$', views.contactform, name='contact'),
    url(r'contact/thanks/$', views.thanks, name='thanks'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)