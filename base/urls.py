from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, CustomRegister

urlpatterns  = [
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', TaskDetail.as_view(), name="taskDetail"),
    path('create/', TaskCreate.as_view(), name='taskCreate'),
    path('edit/<int:pk>', TaskUpdate.as_view (), name='taskUpdate'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='taskDelete'),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegister.as_view() , name='register')
]