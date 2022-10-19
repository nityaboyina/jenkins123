from django.contrib import admin
from .models import User,excel_file
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(excel_file,ImportExportModelAdmin)

