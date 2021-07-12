from django.urls import path

from . import views

urlpatterns = [
    path('insert/', views.insert_text),
    path('table/', views.table, name='table'),
    path('industry/', views.industryOp, name='industry'),
    path('sellInfo/', views.sellInfoOp, name='sellInfo'),
    path('sellTable/', views.toSell),
    path('error/', views.toError),
    path('lr/', views.toLr),
    path('register/', views.userOP)
]