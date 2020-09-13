from django.contrib import admin
from .models import Сategory, Subcategory, Employment_type, Skill, Vacancie

import datetime

from .models import AdvUser
from .utilities import send_activation_notification

# Register your models here.


class VacancieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'email', 'location', 'company')
    list_display_links = ('title', 'category')
    search_fields = ('title', 'category', 'description')


admin.site.register(Vacancie, VacancieAdmin)


admin.site.register(Сategory)
admin.site.register(Subcategory)
admin.site.register(Employment_type)
admin.site.register(Skill)


###

# admin.site.register(AdvUser)

def send_activation_notifications(modeladmin, request, queryset):
        for rec in queryset:
            if not rec.is_activated:
                send_activation_notification(rec)
            modeladmin.message_user(request, 'Alert emails sent')
        send_activation_notifications.short_description = 'Sending Activation Alerts'


class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Activated?'
    parameter_name = 'actstate'
    def lookups(self, request, model_admin):
        return (
                ('activated', 'Gone'),
                ('threedays', 'More than 3 days have passed'), ('week', 'Not more than a week has passed'),
                )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
             d = datetime.date.today() - datetime.timedelta(days=3)
             return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt = d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt = d)

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'), ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)

admin.site.register(AdvUser,AdvUserAdmin)