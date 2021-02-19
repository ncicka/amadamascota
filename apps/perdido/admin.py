from django.contrib import admin

from .models import Mascota, Perdido, Usuario
#from . import models
# Register your models here.

admin.site.register(Mascota)
admin.site.register(Perdido)
admin.site.register(Usuario)