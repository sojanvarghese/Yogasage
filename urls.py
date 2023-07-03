
from django.contrib import admin
from django.urls import path
from yogasage import views
from django.conf import settings
from django.conf.urls.static import static

app_name='yogasage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('details/', views.details,name='details'),
    path('getstarted/', views.getstarted,name='getstarted'),
    path('uday1/', views.uday1,name='uday1'),
    path('uday2/', views.uday2,name='uday2'),
    path('nday1/', views.nday1,name='nday1'),
    path('nday2/', views.nday2,name='nday2'),
    path('oday1/', views.oday1,name='oday1'),
    path('oday2/', views.oday2,name='oday2'),
    path('treepose/', views.treepose,name='treepose'),
    path('easy/', views.easy,name='easy'),   
    path('diamond/', views.diamond,name='diamond'),
    path('goddess/', views.goddess,name='goddess'),    
    path('triangle/', views.triangle,name='triangle'),
    path('warrior/', views.warrior,name='warrior'),
    path('End/', views.End,name='Emd'),
       
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
