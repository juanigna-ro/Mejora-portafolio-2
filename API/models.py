
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#manager para perfiles de usuario
#nos ayuda a manipular los objetos de usuarios
class UserProfileManager(BaseUserManager):
    #creamos un nuevo usuario 
    def create_user(self,email,name,tarjeta,password=None):
        if not email:
            raise ValueError('debe tener email')
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)
        user.set_password(password)
        tarjeta = self.model(tarjeta)
        user.save(using=self.db)
        return user
    #creamos un super usuario
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

#Aqui creamos los modelos para BD en codigo python.
#Estos seran visualizados por DB broser sql
#crearemos la clase usuario que estara asociado una tarjeta

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']

    #obtenemos el nombre completo
    def get_full_name(self):
        return self.name
    #obtenemos nombre corto
    def get_short_name(self):
        return self.name
    #retorn cadena representando a nuestro usuario
    def __str__(self) :
        return self.email


#esta tarjeta estara asociada a un usuario 'regular' no un superuser
class Tarjeta(models.Model):
    nrotarjeta=models.PositiveIntegerField(max_length=16)
    cvv=models.PositiveIntegerField(max_length=3)
    usuario = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    #funcion tarjet
    def creartarjet(self):
        print('tarjeta')
        return self.creartarjeta
    #creamos cvv
    def crearcvv(self):
        print('cvv')
        return self.crearcvv
    #creamos funciones de numeros aleatorios para la creacion de las    #tarjetas tanto para el nro y el cvv


#por ultimo buscaremos la forma de "borrar" los modelos antiguos i/o actualizar los que ya estan. en este caso digitamos el codigo de migraciónes en este orden:
#python manage.py makemigrations API
#python manage.py migrate

class Project(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name