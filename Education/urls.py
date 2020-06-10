from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.about,name='about'),
    path('contactus/',views.contact,name='contact'),
    path('studymaterial/',views.studymaterial,name='study'),
    path('archive/<int:pk>/',views.archive,name='archive'),
    path('blogs/<int:pk>/',views.blogs,name='blogs'),
    path('view/<int:pk>/',views.view,name='view'),
    path('downloads/',views.downloads,name='downloads'),
    path('courses/',views.courses,name='courses'),
    path('viewcourses/<int:pk>/',views.viewcourses,name='viewcourses'),
    
]