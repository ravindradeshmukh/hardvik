from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hardvick import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',views.home, name="home"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

