from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^mantenimientousuarios', views.mantenimientousuarios, name='mantenimientousuarios'),
        url(r'^calendario', views.calendario, name='calendario'),
        url(r'^eventos', views.eventos, name='eventos'),
        url(r'^reporteasistencia', views.reporteasistencia, name='reporteasistencia'),
        url(r'^viaticos', views.viaticos, name='viaticos'),
        url(r'^retrospectiva', views.retrospectiva, name='retrospectiva'),
        url(r'^registroestudiantes', views.registroestudiantes, name='registroestudiantes'),
]
