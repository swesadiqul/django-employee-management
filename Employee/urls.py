from django.urls import path
from Employee import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('emp_login/', views.emp_login, name='emp_login'),
    path('emp_home/', views.emp_home, name='emp_home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('my_experience/', views.my_experience, name='my_experience'),
    path('edit_myexperience/', views.edit_myexperience, name='edit_myexperience'),
    path('my_education/', views.my_education, name='my_education'),
    path('edit_myeducation/', views.edit_myeducation, name='edit_myeducation'),
    path('change_password/', views.change_password, name='change_password'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/', views.all_employee, name='all_employee'),
    path('edit_profile/<int:pid>/', views.edit_profile, name='edit_profile'),
    path('edit_education/<int:pid>/', views.edit_education, name='edit_education'),
    path('edit_experience/<int:pid>/', views.edit_experience, name='edit_experience'),
    path('delete_employee/<int:pid>/', views.delete_employee, name='delete_employee'),
]
