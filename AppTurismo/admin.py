from django.contrib import admin

from AppTurismo.models import Distrito, Estructura, UsuarioCliente, ZonaTuristica

# Register your models here.

admin.site.register(Distrito)
admin.site.register(Estructura)
admin.site.register(ZonaTuristica)
admin.site.register(UsuarioCliente)