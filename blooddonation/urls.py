from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('userreg/',views.userreg,name='userreg'),
    path('insertuser/',views.insertuser,name='insertuser'),
    path('updateuser/',views.updateuser,name='updateuser'),
    path('updateuser/updatedetails/',views.updatedetails,name='updatedetails'),
    path('updateb/<int:uid>/', views.updateb, name='updateb'),
    path('display',views.display,name='display'),
    path('detail',views.detail,name='detail'),
    path('delete',views.delete,name='delete'),
    path('deletedetails',views.deletedetails,name='deletedetails'),
    
     
]
