
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import maximum_number_view
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage,name='signupPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('dashBoardPage/',dashBoardPage,name='dashBoardPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('addJobPage/',addJobPage,name='addJobPage'),
    path('viewJobPage/',viewJobPage,name='viewJobPage'),
    path('jobapplyPage/<str:myid>',jobapplyPage,name='jobapplyPage'),
    path('maximum-number/', maximum_number_view, name='maximum_number'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
