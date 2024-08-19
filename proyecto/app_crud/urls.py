from django.urls import path
from . views import listaEmpleados,crear_empleado,eliminar_empleado
from . import views


urlpatterns = [
    path('', listaEmpleados.as_view(), name='listaEmpleados'),


    #path('detalles_empleado/<str:id>/', views.detalles_empleado, name='detalles_empleado'),
    path('crear_empleado/', crear_empleado.as_view(), name='crear_empleado'),
    path('editar-empleado/<int:pk>/', views.editar_empleado.as_view(), name='editar-empleado'),
    path('eliminar-empleado/<int:pk>/', views.eliminar_empleado.as_view(), name='eliminar-empleado'),
    
    
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    
    
]



