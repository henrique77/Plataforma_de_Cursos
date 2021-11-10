from django.db import models
from django.urls import reverse


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description_icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado em:', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em:', auto_now=True
    )

    object = CourseManager()

    #Representação de string com o nome do curso no model
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/cursos/' + self.slug
        #return ('courses:details', (), {'slug':self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
