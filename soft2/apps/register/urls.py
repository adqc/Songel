from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^registro$', views.registro),
    url(r'^agregarAsesoria$', views.agregarAsesoria),
    url(r'^add$', views.add),
    url(r'^listarAsesoria$', views.listarAsesoria),
    url(r'^eliminarAsesoria$', views.eliminarAsesoria),
    url(r'^editarAsesoria$', views.editarAsesoria),
    url(r'^guardarCambios$', views.guardarCambios),
    url(r'^cancelar$', views.cancelar),
    url(r'^salir$', views.salir),
]
