

from django.urls import path
from laboratorio.views import agregar, informacion, actualizar, eliminar, eliminar_confirmar


urlpatterns = [
    path('', agregar, name='agregar'),
    path('informacion/', informacion, name='informacion'),
    path('informacion/actualizar/<int:id>', actualizar, name='actualizar'),
    path('informacion/eliminar/<int:id>', eliminar, name='eliminar'),
    path('informacion/eliminar_confirmar/<int:id>', eliminar_confirmar, name='eliminar_confirmar'),
]