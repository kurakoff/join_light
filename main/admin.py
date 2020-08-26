from django.contrib import admin
from .models import Сategory, Subcategory, Employment_type, Skill, Vacancie

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
