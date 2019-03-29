"""travel2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
import core.views as views
from django.conf import settings
from django.conf.urls.static import static
from jet_django.urls import jet_urls
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('reservations/new/<int:id>', views.NewReservationView.as_view()),
    path('reservations/', views.ReservationView.as_view()),
    path('trips/<int:id>', views.TripView.as_view()),
    path('jet/', include(jet_urls)),  # Django JET URLS
    path('accounts/signup/', views.signup),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('script/', views.Script.as_view()),
    path('admin/', admin.site.urls),
    path('<order>/', views.IndexView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
