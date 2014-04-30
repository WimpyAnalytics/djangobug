from django.contrib import admin

import models


class SomeDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.SomeData, SomeDataAdmin)
