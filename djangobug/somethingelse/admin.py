from django.contrib import admin

import models


class OtherDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.OtherData, OtherDataAdmin)

