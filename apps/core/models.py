from django.db import models
from ckeditor.fields import RichTextField


# Modelo base personalizado que heredará campos a los demás modelos
class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    creation_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    removal_date = models.DateField('Fecha de Eliminación', auto_now = True, auto_now_add = False)

    # Evita que el modelo base se envíe a la base de datos, sólo añade atributos a los demás modelos que heredarán
    class Meta:
        abstract = True

# Modelos que estarán en la base de datos
class Category(BaseModel):
    name = models.CharField('Nombre de Categoría', max_length = 50, unique = True)
    reference_image = models.ImageField('Imagen de Referencia', upload_to = 'category/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Author(BaseModel):
    name = models.CharField('Nombres', max_length = 50)
    last_name = models.CharField('Apellidos', max_length = 80)
    email = models.EmailField('Correo Electrónico', max_length = 80)
    description = models.TextField('Descripción')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.name)

class Post(BaseModel):
    title = models.CharField('Título del Post', max_length = 80, unique = True)
    slug = models.CharField('Slug', max_length = 80, unique = True)
    description = models.TextField('Descripción')
    author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Categoría')
    content = RichTextField('Contenido')
    reference_image = models.ImageField('Imagen de Referencia', upload_to = 'images/', max_length = 255)
    published = models.BooleanField('Publicado / No Publicado', default = False)
    pub_date = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


# Datos de propietarios de la página
class Web(BaseModel):
    we = models.TextField('Nosotros')
    phone = models.CharField('Teléfono', max_length = 12)
    email = models.EmailField('Correo Electrónico', max_length = 80)
    address = models.CharField('Dirección', max_length = 100)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.we

class SocialNetworks(BaseModel):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

class Contact(BaseModel):
    name = models.CharField('Nombre', max_length = 50)
    last_name = models.CharField('Apellidos', max_length = 80)
    email = models.EmailField('Correo Electrótico', max_length = 80)
    subject = models.CharField('Asunto', max_length = 80)
    message = models.TextField('Mensaje')


    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.subject

class Subscribers(BaseModel):
    email = models.EmailField('Correo Electrónico', max_length = 80)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email



