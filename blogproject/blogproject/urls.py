from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('formcreate/', views.formcreate, name='formcreate'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('detail/<int:blog_id>/', views.detail, name='detail')
]