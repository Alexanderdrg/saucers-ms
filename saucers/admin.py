from django.contrib import admin

from saucers.models import Saucer, Additional, Ingredient


# Register your models here.

admin.site.register(Saucer)
admin.site.register(Ingredient)
admin.site.register(Additional)
