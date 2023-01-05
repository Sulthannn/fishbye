"""penangkapan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from tangkap_app.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('halamantangkapan/', halamantangkapan, name='halamantangkapan'),
    path('tambahtangkapan/', tambahtangkapan),
    path('halamantangkapan/updatetangkapan/<int:id>', updatetangkapan, name='update'),
    path('halamantangkapan/deletetangkapan/<int:id>', deletetangkapan, name='delete'),
    path('halamanadmin/', halamanadmin, name='halamanadmin'),
    path('tambahnelayan/', tambahnelayan),
    path('halamanadmin/updatenelayan/<int:qr>', updatenelayan, name='update2'),
    path('halamanadmin/deletenelayan/<int:qr>', deletenelayan, name='delete2'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('registrasi/', registrasi, name='registrasi'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
