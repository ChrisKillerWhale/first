from django.conf.urls import url
# . meaning from current app
from . import views

urlpatterns = {
    url(r'^$', views.store, name='index'),
}
