from django.contrib import admin
from pruebaApp.models import Juguete, Libro, Ropa

# Register your models here.
class JugueteAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","codigoProducto"]

class LibroAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","codigoProducto"]

class RopaAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","codigoProducto"]

admin.site.register(Juguete, JugueteAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ropa, RopaAdmin)


