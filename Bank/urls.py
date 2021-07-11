from django.urls import path
from .import views
urlpatterns = [
    path('transactions',views.showtransactions,name='showusers12'),
    path('selectuser',views.showusers,name='trial'),
    path('selectuser/<str:name>',views.nameuser,name='showusers'),
    path('selectuser/<str:name>/show.html',views.insert1,name='showusers1'),

]