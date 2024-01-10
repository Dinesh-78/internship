from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.index,name='index'),
   path('login/',views.loginpage,name='loginpage'),
   path('register/',views.registerpage,name='registerpage'),
   path('doctor/',views.doctorpage,name='doctorpage'),
   path('Patient/',views.patientpage,name='patientpage'),
   path('myprofile/',views.MyProfile,name='myprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)