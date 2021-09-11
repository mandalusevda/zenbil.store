from django.urls import path
from django.views import generic
from . import views
from django.conf.urls.static import static
from django.conf import settings

appname='product'
urlpatterns = [
    path('create', views.create,name='product_create'),
    path('post',views.postx,name='product_post'),
    # path('/post',views.posty,name='product_post'),
    path('detail', views.detail,name='product_detail'),
    # path('home', views.ListView,name='home1'),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
