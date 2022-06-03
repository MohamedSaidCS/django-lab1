from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.show, name='show'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('<int:todo_id>/done', views.mark_done, name='done'),
    path('<int:todo_id>/edit', views.edit, name='edit'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
]
