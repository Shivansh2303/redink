from django.contrib import admin
from django.urls import path
from PrintFac import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/upload', views.FileUploadView, name ='file-upload'),
    path('success/',views.HandleSuccess,name='payment-success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    