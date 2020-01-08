from tutorial import views	
from django.urls import include, re_path

app_name = 'tutorial'
urlpatterns = [
  # The home view ('/tutorial/')
  re_path(r'^$', views.home, name='home'),
  # Explicit home ('/tutorial/home/')
  re_path(r'^home/$', views.home, name='home'),
  re_path(r'^gettoken/$', views.gettoken, name='gettoken'),
  re_path(r'^mail/$', views.mail, name='mail'),
  re_path(r'^events/$', views.events, name='events'),
  re_path(r'^contacts/$', views.contacts, name='contacts'),

]