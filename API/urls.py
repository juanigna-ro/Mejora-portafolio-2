#se creao este .py para exportar de maneta general los views
from cgitb import html
from django.urls import URLPattern
from django.urls import path
from . import views

#se le agrego "cron" al path cron.opkm para acceder a el.

urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('hola/<int:id>',views.hello),
    path('project',views.project),
    path('task/<int:id>',views.task),
    path('create_task/',views.create_task),
    path('iniciomatch/',views.iniciomatch),
]