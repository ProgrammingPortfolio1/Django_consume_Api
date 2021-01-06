from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('info/<int:userid>', views.info, name='info'),

    path('posts/<int:userid>', views.posts, name='posts'),

    path('photos/<int:userid>', views.photos, name='photos'),

]


handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'
