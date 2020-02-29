from django.conf.urls import url
from basic_app import views


urlpatterns = [

    url(r'^$',views.forms_page,name="forms_page"),
 ]
