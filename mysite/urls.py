from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup.html'),
    path('tasks/', views.tasks, name='tasks'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    #path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
    path('generar_pdf/<int:task_id>/', views.generar_pdf, name='generar_pdf'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    
]
