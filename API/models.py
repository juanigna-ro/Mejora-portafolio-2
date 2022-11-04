
from email.policy import default
from django.db import models

#Aqui creamos los modelos para BD en codigo python.
#Estos seran visualizados por DB broser sql

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