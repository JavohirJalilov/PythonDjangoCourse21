from django.contrib import admin

# Register your models here.
from .models import Metup,Location

class MetupAdmin(admin.ModelAdmin):
	list_display = ('title','slug')
	prepopulated_fields = {'slug':('title',)}
admin.site.register(Metup,MetupAdmin)
admin.site.register(Location)

