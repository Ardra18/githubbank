from django.urls import path
from . import views
app_name='bank'
urlpatterns=[
    path('',views.index,name='index'),
    path('trv',views.trv,name='trv'),
    path('kol', views.kol, name='kol'),
    path('alapuzha',views.alapuzha,name='alapuzha'),
    path('ekm',views.ekm,name='ekm'),
    path('kannur',views.kannur,name='kannur'),



]