from django.conf.urls import url 
from . import views

#Template tagging

app_name = 'basic_app'


urlpatterns = [url(r'^other/$',views.other,name='other'),
url(r'^relative/$',views.relative,name = 'relative'),
]

