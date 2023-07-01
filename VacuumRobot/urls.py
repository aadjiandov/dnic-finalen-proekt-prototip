"""
URL configuration for VacuumRobot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import robots_list, about, contact, robot_search, add_to_cart, cart, checkout, delete_from_cart, update_quantity
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('robots/', robots_list, name='robots'),
                  path('about/', about, name='about'),
                  path('contact/', contact, name='contact'),
                  path('robots/search/', robot_search, name='robot_search'),
                  path('cart/', cart, name='cart'),
                  path('add-to-cart/<int:robot_id>/', add_to_cart, name='add_to_cart'),
                  path('checkout/', checkout, name='checkout'),
                  path('delete_from_cart/<int:robot_id>/', delete_from_cart, name='delete_from_cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
