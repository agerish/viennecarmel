
from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('abonner/',views.add),
    path('contact/',views.contact),
    path('',views.index)

]
