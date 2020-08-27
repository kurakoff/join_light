from django.db import models

# Create your models here.


# Create your models here.
class Сategory(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Сategory'
        ordering = ['name']


class Subcategory(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')
    img = models.ImageField(upload_to='img/subcategory', null=True, verbose_name='Subcategory_img')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subcategories'
        verbose_name = 'Subcategory'
        ordering = ['name']

class Employment_type(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employments'
        verbose_name = 'Employment'
        ordering = ['name']


class Skill(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ['name']


class Vacancie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    category = models.ForeignKey('Сategory', null=True, on_delete=models.PROTECT, verbose_name='Сategory')
    subcategores = models.ManyToManyField('Subcategory', verbose_name='Subcategory')
    employment = models.ForeignKey('Employment_type', null=True, on_delete=models.PROTECT, verbose_name='Employmet type')
    skill = models.ForeignKey('Skill', null=True, on_delete=models.PROTECT,
                                   verbose_name='Skill')
    img = models.ImageField(upload_to='img', null=True, verbose_name='Vacancy_img'
                            )
    email = models.EmailField(max_length=50, verbose_name='Email')
    location = models.TextField(null=True, blank=True, verbose_name='Location')
    salary = models.FloatField(null=True, blank=True)
    company = models.CharField(max_length=70, null=True, blank=True,verbose_name='Company')
    url = models.CharField(max_length=50, null=True, blank=True, verbose_name='Url')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    requirements = models.TextField(null=True, blank=True, verbose_name='requirements')
    tasks = models.TextField(null=True, blank=True, verbose_name='Tasks')
    terms = models.TextField(null=True, blank=True, verbose_name='Terms')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Vacancies'
        verbose_name = 'Vacancy'
        ordering = ['-published']

