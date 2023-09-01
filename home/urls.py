from django.urls import path
from home import views
urlpatterns = [
    #it will take you to the homepage index.html
    path('',views.index,name='index'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updateRecord/<int:id>',views.updateRecord,name='updateRecord'),
    path('update_chart/',views.update_chart,name='update_chart')
]