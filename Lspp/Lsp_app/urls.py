from django.conf.urls import url
from . import views

app_name = 'Lsp_app'
urlpatterns = [
    url(r'^$', views.all_patients, name='all_patients'),
    url('/Lsp_app/', views.get_patient, name='get_patient'),

]
