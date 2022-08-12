from django.conf import settings
from django.urls import path
from . import views



urlpatterns = [
path('', views.holamundocore, name='core'),
path('nosotros',views.nosotros, name='nosotros'),
path('productos', views.productos, name='productos'),
path('contactanos',views.contactanos, name='contactanos'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
