from django import views
from django.urls import path
from .views import index_view, features, contact,image_upload_page, login_user, logout_user, register_user, report,result_chart 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index_view, name='index_view'),
    path('features/', features, name='features'),
    path('contact/', contact, name='contact'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
    path('image_upload_page/', image_upload_page,name='image_upload_page'),
    path('ResultChart/',result_chart,name='result_chart'),
    path('report/',report,name='report'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
