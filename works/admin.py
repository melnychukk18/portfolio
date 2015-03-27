from django.contrib import admin
from works.models import WorkItem, WorkImage

class BasicAdmin(admin.ModelAdmin):
    pass

admin.site.register(WorkItem, BasicAdmin)
admin.site.register(WorkImage, BasicAdmin)
