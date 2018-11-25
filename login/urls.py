from django.conf.urls import url
from login import views

app_name = 'login'

urlpatterns = [

url(r'^$',views.index,name='index'),
url(r'^PNB/',views.auth,name='PNB'),
url(r'^SBI/',views.auth,name='SBI'),
url(r'^home/',views.home,name='home')

]