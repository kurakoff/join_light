from django.conf.urls import url
from django.urls import path

from . import views
from .views import index, by_category, book_detail_view
from django.conf import settings
from django.conf.urls.static import static
from .views import other_page

from django.urls import reverse_lazy



#

from .views import JobLoginView
from .views import profile
from .views import JobLogoutView
from .views import ChangeUserInfoView
from .views import JobPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate
from .views import DeleteUserView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


app_name = 'main'
urlpatterns = [
    path('<int:category_id>/', by_category, name="by_category"),
    path('vacancy/<int:vacancy_id>/', book_detail_view, name="vacancy"),
    path('', index, name='index'),
    path('contact/', views.contactform, name='contact'),
    path('contact/thanks/', views.thanks, name='thanks'),
    path('<str:page>/', other_page, name='other') ,

    path('accounts/login/', JobLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', JobLogoutView.as_view(), name='logout'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('acoounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', JobPasswordChangeView.as_view(), name='password_change'),
    path('acoounts/register/done/', RegisterDoneView.as_view(), name="register_done"),
    path('acoounts/register/', RegisterUserView.as_view(), name="register"),
    path('acoounts/register/activate/<str:sign>/', user_activate, name='register_activate'),

    path('accounts/password_reset', PasswordResetView.as_view(template_name="registration/reset_password.html",
                                                              subject_template_name='email/reset_subject.txt',
                                                              email_template_name='email/reset_email.html',
                                                              success_url=reverse_lazy('main:password_reset_done')),
         name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/email_sent.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/confirm_password.html', success_url=reverse_lazy(
             'main:password_reset_complete')), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_confirmed.html'),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)