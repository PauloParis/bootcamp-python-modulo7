from django.contrib import admin

# Register your models here.


from laboratorio.models import Laboratorio, DirectorGeneral, Producto


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

