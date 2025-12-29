from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),   # ✅ ADD THIS
     path('signup/', views.signup_view, name='signup'), 
    path('apply/', views.apply_leave, name='apply_leave'),
    path('my/', views.my_leaves, name='my_leaves'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    path('update/<int:id>/<str:status>/', views.update_status, name='update_status'),
]
