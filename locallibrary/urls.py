"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
# use include() to add urls from the catalog application and authentication system
from django.conf.urls import url, include
# use static() to add url mapping to serve static files during development only
from django.conf.urls.static import static
from django.contrib import admin
# use url maps to redirect the base url to our application
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
